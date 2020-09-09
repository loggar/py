import subprocess
from pathlib import Path

file_path = Path.home()/'my-data-here'
for audio_file in list(file_path.glob('*.wav')):
    cmd = ['ffmpeg',
           '-i',
           str(audio_file),
           f'{audio_file.name.split(".")[0]}.flac']
    subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
