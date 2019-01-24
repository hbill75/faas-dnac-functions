import requests
import json

def handle(req):

    req_info = json.loads(req)
    url = "https://api.ciscospark.com/v1/messages"
    messagePayload = json.dumps({"roomId": req_info["roomId"],
    "text": req_info["messageBody"]})
    payload = messagePayload
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + req_info["teams_token"]
        }

    uptimeMessage = requests.request("POST", url, data=payload, headers=headers)
    return uptimeMessage.text
