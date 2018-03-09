# Hackathon
IBM Hackathon - Transcript Generator Realtime using Watson Api

Apis Used : Google Speech to Text - (English , Hindi , Telugu, Tamil)
            Watson Tone analyser 
            Text Summarizer - Deep.ai

How to run : 
	1. Go to the Hackathon folder
	2. Run python2 main.py after installing all the dependencies below
	3. Remember to stop the recognition you have to say exit

Dependencies :
	python packages : pyaudio, google.cloud , filetype , tinytag, pyqt4 , requests

For other languages the output is shown only on command line.


Work Flow :

	1) Use Google API to convert live stream audio to text
	2) Use the IBM watson api to extract tones / emotions from the above generated text
	3) Use the deep.ai api to summarize the text generated in step-1
