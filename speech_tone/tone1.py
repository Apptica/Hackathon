import requests

def tone(data):
	headers = {'Content-Type': 'text/plain',}
	params = (('version', '2017-09-21'),)
	response = requests.post('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone', headers=headers, params=params, 
		data=data, auth=('c793adad-7004-4379-a188-ddb6b512bdf4', 'KuhhOW0rodyk'))
	return response.text


data = '''Welcome to the IBM Hackathon hosted in IIIT Jabalpur and this is your host joining you to give live updates about the ongoings here. The participants here are looking very excited about the contest. Some of them look nervous while the others are looking confident to win the contest.'''
print tone(data)