import tone_analyser
import speech_google
import json

data = speech_google.main()

#data = '''Welcome to the IBM Hackathon hosted in IIIT Jabalpur and this is your host joining you to give live updates about the ongoings here. The participants here are looking very excited about the contest.'''
print "Final Output: \""+data + "\""


tone_json = tone_analyser.tone(data)
parsed = json.loads(tone_json)
print json.dumps(parsed, indent=4, sort_keys=True)
