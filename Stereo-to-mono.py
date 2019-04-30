import os

def st2mono(arquivo):
    from pydub import AudioSegment
    
    if arquivo.endswith('.wav'):
    	sound=AudioSegment.from_wav(arquivo)
    	sound=sound.set_channels(1)
    	output="[MONO] %s"%(arquivo)
    	print("%s criado."%output)
    	sound.export(output, format="wav")

    if arquivo.endswith('.mp3'):
    	sound=AudioSegment.from_mp3(arquivo)
    	sound=sound.set_channels(1)
    	output="[MONO] %s"%(arquivo)
    	print("%s criado."%output)
    	sound.export(output, format="mp3")    


for f in os.listdir():
     if (f.endswith('.wav') or f.endswith('.mp3')) and not f.startswith('[MONO]'):
         st2mono(f)