import requests
import json


username = "devnetuser"
password = "Cisco123!"
webex_teams_token = "MDE3Njk1YTEtNWIxZi00YjMwLWEwMzctODQ5NTIzMWE1ZmMzNTQ3ODJjMWEtZmI5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vZjhiM2QyZDAtMWY1MC0xMWU5LTg5NGUtYzdkYjJmNjhjZTMw"

"""
Get the DNA Center auth token for the user: devnetuser by invoking the
dnacsandbox-auth function.  Send the DNA Center username and password in the
POST method payload.
"""

authurl = "http://127.0.0.1:31112/function/dnacsandbox-auth"
userpass = json.dumps({"username": username, "password": password})
payload = userpass
headers = {
    'Content-Type': "application/json",
    }

token = requests.request("POST", authurl, data=payload, headers=headers)

print("This is the devnetuser's DNA Center Auth Token\n")
print(token.text)

"""
Get all of the devices DNA Center knows about using the dnacsandbox-getdevices
function. Send the returned auth token in the POST method payload.
"""

getdeviceurl = "http://127.0.0.1:31112/function/dnacsandbox-getdevices"
payload = token.text
headers = {
    'Content-Type': "application/json"
    }

devices = requests.request("POST", getdeviceurl, data=payload, headers=headers)

print("These are details of all the devices known by DNA Center\n")
print(devices.text)

"""
Parse the device details returned from the dnacsandbox-getdevices function
and extract the Hostname, Device type and up time to build the message being
sent to webex teams.
"""

activedevices = json.loads(devices.text)

messageBody = ""

for deviceDetails in activedevices["response"]:
    type = deviceDetails["type"]
    hostname = deviceDetails["hostname"]
    upTime = deviceDetails["upTime"]
    messageBody = messageBody + "Hostname: {0}\nType: {1}\nUp Time {2}\n\n".format(hostname, type, upTime)

"""
Send the formatted device uptime message to a webex teams space using the
postdeviceuptime function.  Send the Webex teams Room ID, Message and your webex
Teams developer token in the POST method payload.
"""
messagePayload = json.dumps({"roomId": roomId,
                             "messageBody": messageBody,
                             "teams_token": webex_teams_token})
postmessageurl = "http://127.0.0.1:31112/function/postdeviceuptime"

payload = messagePayload
headers = {
    'Content-Type': "application/json"
    }

uptimeMessage = requests.request("POST", postmessageurl, data=payload, headers=headers)

print("This is the successful message response\n")
print(uptimeMessage.text)
