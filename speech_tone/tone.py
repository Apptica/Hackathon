import requests

headers = {
    'Content-Type': 'application/json',
}

params = (
    ('version', '2017-09-21'),
)

data = open('tone.json', 'rb').read()
response = requests.post('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone', headers=headers, params=params, 
	data=data, auth=('c793adad-7004-4379-a188-ddb6b512bdf4', 'KuhhOW0rodyk'))

print response.text