from dataclasses import dataclass


@dataclass
class HtmlRequests:
    def __init__(self, get=[], post=[], put=[], delete=[], patch=[]):
        self.get = []
        self.post = []
        self.put = []
        self.delete = []
        self.patch = []

def run(self, request):
    return [vulnerabilityTest(request) for vulnerabilityTest in getattr(self, request.type)]
