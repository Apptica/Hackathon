import os
import io
import json
from tinytag import TinyTag
import filetype
import tone_analyser
import speech_google
TONE_FILE = "tone_output.txt"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='backup/auth.json'
def transcribe_streaming(stream_file):
    """Streams transcription of the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()
    tag = TinyTag.get(stream_file)
    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()
    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]
    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)
    kind = filetype.guess(stream_file)
    codec = enums.RecognitionConfig.AudioEncoding.LINEAR16
    if(kind.extension=='flac'):
        codec = enums.RecognitionConfig.AudioEncoding.FLAC
    config = types.RecognitionConfig(
        encoding=codec,
        sample_rate_hertz=tag.samplerate,
        language_code='en-US')
    streaming_config = types.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(streaming_config, requests)
    ans = ""
    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print('Finished: {}'.format(result.is_final))
            print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print('Confidence: {}'.format(alternative.confidence))
                print('Transcript: {}'.format(alternative.transcript))
                ans = ans + str(alternative.transcript)

    tones = ''
    tone_json = json.loads(tone_analyser.tone(ans))
    if tone_json.has_key('document_tone') :
        if tone_json['document_tone'].has_key('tones'):
            for res in tone_json['document_tone']['tones']:
                    tones += ('\t' + res['tone_name'] + ' - ' + str(res['score']*100) + ' %\n');

    file = open(TONE_FILE, "w")
    if not tones == ''  :
        #print('Tones Detected:: \n' + tones)
        file.write('Tones Detected:: \n' + tones)
    else:
        #print('No Tones Detected.\n')
        file.write('No Tones Detected.\n')
    file.close()
    return ans
