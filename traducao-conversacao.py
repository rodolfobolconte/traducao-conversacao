import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("A:/Downloads/Temporário/hello.mp3")
play_obj = wave_obj.play()
play_obj.wait_done()

exit()

from googletrans import Translator

texto = "How old are you?"

tradutor = Translator()

print(tradutor.translate(texto, dest='pt').text)