from IPython.display import Audio
from melo.api import TTS
import soundfile as sf
import io

device = 'auto'
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id

jobs = {}

def tts_to_audio(text, job_id, speacker_id="EN-US"):
  sample_rate = 44100
  audio = model.tts_to_file(text, speaker_ids[speacker_id])
  
  audio_buffer = io.BytesIO()
  
  sf.write(audio_buffer, audio, sample_rate, format='WAV')
  
  audio_buffer.seek(0)
  
  print("object created")
  
  jobs[job_id] = audio_buffer