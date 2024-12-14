from dataclasses import dataclass
from vulnerability_testers import *
from pprint import pprint
import requests


@dataclass
class HtmlRequests:
    def __init__(
        self,
        url,
        securitySchemes,
        stopOnFailure,
        statusCodeValidation,
        dosRequestCount,
        maxAcceptableResponseTime,
        endpointsWithoutAuth,
    ):
        self.url = url
        self.securitySchemes = securitySchemes
        self.stopOnFailure = stopOnFailure
        self.statusCodeValidation = statusCodeValidation
        self.dosRequestCount = dosRequestCount
        self.maxAcceptableResponseTime = maxAcceptableResponseTime
        self.endpointsWithoutAuth = endpointsWithoutAuth
        self.authenticate(
            "/users/v1/login",
            {"username": "name1", "password": "pass1"},
        )

    def authenticate(self, login_path, login_payload):
        login_url = f"{self.url}{login_path}"
        try:
            response = requests.post(login_url, json=login_payload)
            if response.status_code == 200:
                # Extract token from response (modify this based on API's token format)
                self.token = response.json().get("auth_token")
            else:
                print(
                    f"Authentication failed with status code {response.status_code}: {response.text}"
                )
        except requests.RequestException as e:
            print(f"Error during authentication: {e}")

    def run(self, request, is_endpoint_secured=True):
        outputs = []
        cmd_injection(request, self.url)
        outputs.append(
            dos(
                self.url,
                request,
                self.dosRequestCount,
                self.maxAcceptableResponseTime,
            )
        )
        if is_endpoint_secured:
            outputs.append(endpoint_auth(self.url, request, self.endpointsWithoutAuth))
        if request["method"].lower() != "post":
            outputs.append(
                error_codes(
                    self.url,
                    request,
                    self.statusCodeValidation,
                    is_endpoint_secured,
                    self.token,
                )
            )
        if request["method"].lower() == "post":
            outputs.append(file_limits(request))
        outputs.append(
            sql_injection(request, self.url, self.token, is_endpoint_secured)
        )
        # for vulnerabilityTest in getattr(self, request["method"].lower()):
        #     test_output = vulnerabilityTest(request)
        #     outputs.append(test_output)
        #     if self.stopOnFailure and not test_output["passed"]:
        return outputs
