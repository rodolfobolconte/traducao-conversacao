from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

texto = input('Digite um texto: ')

tts = gTTS(texto, lang='pt-br')
arquivo = 'audio.mp3'

#tts.save(arquivo)
#playsound(arquivo)
#os.remove(arquivo)


tradutor = Translator()

print(tradutor.translate(texto, dest='en').text)