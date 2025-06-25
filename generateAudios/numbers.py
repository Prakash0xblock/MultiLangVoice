import os

from gtts import gTTS
from pydub import AudioSegment

# Create output directory
output_dir = 'audio'
os.makedirs(output_dir, exist_ok=True)

# Generate and save Gujarati audio for numbers 1 to 100 in WAV format
for i in range(1, 100):  # include 100
    text = str(i)
    tts = gTTS(text=text, lang='gu')
    mp3_filename = os.path.join(output_dir, f'{i}.mp3')
    wav_filename = os.path.join(output_dir, f'{i}.wav')

    # Save as MP3
    tts.save(mp3_filename)

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(mp3_filename)
    sound.export(wav_filename, format='wav')

    # Remove temporary MP3 file
    os.remove(mp3_filename)

    print(f'Saved: {wav_filename}')
