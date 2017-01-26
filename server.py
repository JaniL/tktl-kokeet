import falcon
import json
from retrieve import fetch_exams, parse_exams

app = falcon.API()

class SeperateExams(object):
    def on_get(self, req, resp):
        exams = parse_exams(fetch_exams())

        resp.body = json.dumps(exams)

seperate_exams = None

app.add_route('/exams', SeperateExams())