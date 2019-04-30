def st2mono(arquivo):
    from pydub import AudioSegment
    sound = AudioSegment.from_wav(arquivo)
    sound = sound.set_channels(1)
    output="[MONO] %s"%(arquivo)
    print("%s salvo na pasta"%output)
    sound.export(output, format="wav")

import os
for f in os.listdir():
     if f.endswith('.wav') and not f.startswith('[MONO]'):
         st2mono(f)