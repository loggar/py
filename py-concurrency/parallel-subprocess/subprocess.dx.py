import subprocess
from pathlib import Path

path = Path.home()/'my-data-here'
for audio_file in list(path.glob('*.wav')):
    cmd = ['ffmpeg',
           '-i',
           str(audio_file),
           f'{audio_file.name.split(".")[0]}.flac']
    subprocess.run(cmd, stdout=subprocess.PIPE)
