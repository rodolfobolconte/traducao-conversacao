from gtts import gTTS
from playsound import playsound
import os

tts = gTTS('Bom dia Rodolfo, você está bem?', lang='pt-br')

arquivo = 'audio.mp3'

tts.save(arquivo)
playsound(arquivo)
os.remove(arquivo)
exit()

from googletrans import Translator

texto = "How old are you?"

tradutor = Translator()

print(tradutor.translate(texto, dest='pt').text)