WEBHOOK_URL = "PUBLIC IP TO RECEIVE THE DATA FROM SPARK"
TOKEN = "YOUR SPARK TOKEN. Get one at developers.spark.com"

import requests
import json

url = "https://api.ciscospark.com/v1/webhooks/"

headers = {
    'content-type': "application/json",
    'authorization': "Bearer " + TOKEN,
    }

def get_webhooks():
	response = requests.request("GET", url, headers=headers)
	json_out = response.json()
	# print (json.dumps(json_out, indent=2))
	ids = []
	for webhook in json_out["items"]:
		#print (webhook["id"])
		ids.append(webhook["id"])
	return ids

def delete_webhook(id):
	delete_url = url + id
	response = requests.request("DELETE", delete_url, headers=headers)

def create_webhook():
	targetUrl = WEBHOOK_URL + "/spark/webhook"
	body = {
	"name": "Test Webhook",
	"targetUrl": targetUrl,
	"resource": "messages",
	"event": "created"
	}	
	response = requests.request("POST", url, json=body, headers=headers)
	json_out = response.json()
	#print(json.dumps(json_out, indent=2))
	print ("Webhook created for " + targetUrl)

try:
	ids = get_webhooks()
	for id in ids:
		delete_webhook(id)
except:
	print ('Could not get webhooks')

create_webhook()
#get_webhooks()
