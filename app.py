import json
import pickle
from chalice import Chalice, Response

from chalicelib import analyze

app = Chalice(app_name="titanic")

request_headers = {"Content-Type": "application/json"}

app.api.cors = True

with open("modelo.pickle", "rb") as arq:
    _modelo = pickle.load(arq)


@app.route("/", methods=["POST"], content_types=["application/json"])
def index():
    try:
        request = app.current_request
        body = request.json_body
        response = analyze.analyze(body, _modelo)
        return Response(
            body=json.loads(json.dumps({"result": response.tolist()})),
            status_code=200,
            headers=request_headers,
        )
    except (TypeError, KeyError) as err:
        return Response(
            body=json.loads(json.dumps({"error": str(err)})),
            status_code=500,
            headers=request_headers,
        )
