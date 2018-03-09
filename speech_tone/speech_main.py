import tone_analyser
import speech_google
import json

data = speech_google.main()

#data = '''Welcome to the IBM Hackathon hosted in IIIT Jabalpur and this is your host joining you to give live updates about the ongoings here. The participants here are looking very excited about the contest.'''

print("\n\nFinal Output: \""+data + "\"\n\n")


tones = ''
tone_json = json.loads(tone_analyser.tone(data))
if tone_json.has_key('document_tone') :
	if tone_json['document_tone'].has_key('tones'):
		for res in tone_json['document_tone']['tones']:
				tones += ('\t' + res['tone_name'] + ' - ' + str(res['score']*100) + ' %\n');

if not tones == ''  :
	print('Tones Detected:: \n' + tones)
else:
	print('No Tones Detected.\n')

#parsed = json.loads(tone_json)
#print json.dumps(parsed, indent=4, sort_keys=True)
