import requests
import os
import json

def getSummary(text):
	f = open('summary.txt', 'w')
	r = requests.post(
	    "https://api.deepai.org/api/summarization",
	    data={
	        'text': text,
	    },
	    headers={'api-key': '418a9720-2b4c-4331-90c0-7b6d48236b59'}
	)
	f.write(Summary/r.json()['output'])
