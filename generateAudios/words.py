import os

from gtts import gTTS
from pydub import AudioSegment

# Create output directory
output_dir = 'audio'
os.makedirs(output_dir, exist_ok=True)

# Gujarati number words for 100 to 1000
gujarati_numbers = {
    100: 'સો',
    200: 'બસો',
    300: 'ત્રણસો',
    400: 'ચારસો',
    500: 'પાંચસો',
    600: 'છાસો',
    700: 'સાતસો',
    800: 'આઠસો',
    900: 'નવસો',
    1000: 'હજાર'
}

# Generate and save Gujarati audio in WAV format
for number, word in gujarati_numbers.items():
    tts = gTTS(text=word, lang='gu')
    mp3_filename = os.path.join(output_dir, f'{number}.mp3')
    wav_filename = os.path.join(output_dir, f'{number}.wav')

    # Save as MP3
    tts.save(mp3_filename)

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(mp3_filename)
    sound.export(wav_filename, format='wav')

    # Remove temporary MP3 file
    os.remove(mp3_filename)

    print(f'Saved: {wav_filename}')
