import os

from playsound import playsound


def get_audio_sequence(num):
    if not (1 <= num <= 9999999):
        raise ValueError('Number must be between 1 and 9999999')

    result = []

    if num >= 100000:
        lakhs = num // 100000
        result.append(lakhs)
        result.append(100000)
        num %= 100000

    if num >= 1000:
        thousands = num // 1000
        result.append(thousands)
        result.append(1000)
        num %= 1000

    if num >= 100:
        hundreds = num // 100
        remainder = num % 100

        if remainder == 0:
            result.append(hundreds * 100)
        else:
            result.append(hundreds)
            result.append(100)
        num = remainder

    if num > 0:
        result.append(num)

    return result

def play_audio_sequence(sequence, base_path='audio'):
    for number in sequence:
        file_path = os.path.join(base_path, f'{number}.wav')
        if os.path.isfile(file_path):
            try:
                playsound(file_path)
            except Exception as e:
                print(f'Error playing {file_path}: {e}')
        else:
            print(f'[Missing] Audio file not found: {file_path}')

if __name__ == '__main__':
    num = 2520
    try:
        sequence = get_audio_sequence(num)
        print(f'{num} → {sequence}')
        play_audio_sequence(sequence)
    except ValueError as e:
        print(f'Error: {e}')