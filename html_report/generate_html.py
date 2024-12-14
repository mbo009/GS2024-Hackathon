import json
from jinja2 import Template
import sys
from pprint import pprint


def load_json(json_path):
    with open(json_path, "r") as fh:
        return json.load(fh)


def group_tests(tests):
    grouped_data = {}
    for test in tests:
        test_type = test["testType"]
        if test_type not in grouped_data:
            grouped_data[test_type] = {"testsPassed": 0, "testsTotal": 0, "details": []}
        grouped_data[test_type]["testsTotal"] += 1
        if test["passed"]:
            grouped_data[test_type]["testsPassed"] += 1

        grouped_data[test_type]["details"].append(
            (test["endpoint"], test["description"])
        )
    pprint(grouped_data)

    return [
        (key, value["testsPassed"], value["testsTotal"], value["details"])
        for key, value in grouped_data.items()
    ]


def generate_html(data, template_path, output_path):
    print(data)
    with open(template_path, "r") as fh:
        template = Template(fh.read())

    html_content = template.render(data=data)

    with open(output_path, "w") as fh:
        fh.write(html_content)


if __name__ == "__main__":
    json_data = load_json("exampleReport.json")
    grouped_data = group_tests(json_data)
    generate_html(grouped_data, "template.html", "generatedReport.html")
