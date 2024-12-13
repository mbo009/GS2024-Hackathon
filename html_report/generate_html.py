import json
from jinja2 import Template
import sys

def load_json(json_path):
    with open(json_path, 'r') as fh:
        return json.load(fh)

def generate_html(data, template_path, output_path):
    print("data", data)
    with open(template_path, 'r') as fh:
        template = Template(fh.read())
    
    html_content = template.render(data=data)

    with open(output_path, 'w') as fh:
        fh.write(html_content)

if __name__ == "__main__":
    # print("ccc")
    json_data = load_json("../exampleReport.json")
    generate_html(json_data, "template.html", "generatedReport.html")