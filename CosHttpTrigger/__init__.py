import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    res = {"msg": "Hello, World!", "desc": "Simple greetings application"}
    return func.HttpResponse(
        json.dumps(res), mimetype="application/json", status_code=200
    )
