from penTester import Pentester
import json
from html_report.generate_html import generate_html

if __name__ == "__main__":
    pentester = Pentester("config.json")
    outputs = pentester.run()

    with open("report.json", "w") as fh:
        json.dump(outputs, fh, indent=4)

    generate_html()
