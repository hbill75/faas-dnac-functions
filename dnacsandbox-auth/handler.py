import requests
import base64
import json

def handle(req):
	req_info = json.loads(req)
	userAndPassword = req_info["username"] + ":" + req_info["password"]
	base64AuthString = base64.b64encode(userAndPassword.encode())
	payload = ""
	headers = {"Authorization": "Basic " + base64AuthString.decode("utf-8")}
	url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.text
