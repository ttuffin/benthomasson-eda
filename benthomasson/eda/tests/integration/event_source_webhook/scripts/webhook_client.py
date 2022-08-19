import requests
import json
from time import sleep

for i in range(10):
    url = "http://127.0.0.1:5000/webhook"
    headers = {"user-agent": "webhook_client/1.0.1"}

    try:
        requests.post(
            url, json.dumps({"ping": "pong"}).encode("ascii"), headers=headers
        )
    except requests.exceptions.ConnectionError:
        sleep(1)
    else:
        requests.post(
            url, json.dumps({"shutdown": ""}).encode("ascii"), headers=headers
        )
        break
