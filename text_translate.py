from google.cloud import translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./speech_tone/auth.json'
def getTranslated():
    translate_client = translate.Client()
    f = open('input2.txt','r')
    text = f.read();
    target = 'en'
    result = translate_client.detect_language(text)
    if(result['language']!=target):
        translation = translate_client.translate(
            text,
            target_language=target)
        print(u'Translation: {}'.format(translation['translatedText']))
getTranslated()