from dataclasses import dataclass
from vulnerability_testers.validate_cmdinjection_vulnerabilities import (
    validate_cmdinjection_vulnerabilities,
)


@dataclass
class HtmlRequests:
    def __init__(
        self, url, stopOnFailure, get=[], post=[], put=[], delete=[], patch=[]
    ):
        self.url = url
        self.stopOnFailure = stopOnFailure
        self.get = [validate_cmdinjection_vulnerabilities]
        self.post = []
        self.put = []
        self.delete = []
        self.patch = []

    def run(self, request):
        outputs = []
        for vulnerabilityTest in getattr(self, request["method"].lower()):
            test_output = vulnerabilityTest(request)
            outputs.append(test_output)
            if self.stopOnFailure and not test_output["passed"]:
                return outputs
