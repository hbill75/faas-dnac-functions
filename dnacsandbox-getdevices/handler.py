import requests
import json

def handle(req):

	json_req  = json.loads(req)
	token = json_req["Token"]
	payload = ""
	headers = {
				"x-auth-token": token,
				"Content-Type": "application/json; charset=utf-8"
				}
	url = "https://sandboxdnac.cisco.com/api/v1/network-device"
	response = requests.request("GET", url, data=payload, headers=headers)
	return response.text
