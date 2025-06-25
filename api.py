import os

from flask import Flask, jsonify, request
from playsound import playsound

app = Flask(__name__)

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

def play_file(name, base_path='wav'):
    path = os.path.join(base_path, f'{name}.wav')
    if os.path.isfile(path):
        try:
            playsound(path)
        except Exception as e:
            print(f'Error playing {path}: {e}')
    else:
        print(f'[Missing] {path}')

def play_token_number(input_text, base_path='audio'):
    input_text = input_text.lower().strip()
    words = input_text.split()
    number = None
    prefix_files = []

    for word in words:
        if word.isdigit():
            number = int(word)
            break
        else:
            prefix_files.append(word)

    for prefix in prefix_files:
        play_file(prefix, base_path)

    if number is not None:
        sequence = get_audio_sequence(number)
        for item in sequence:
            play_file(str(item), base_path)

@app.route('/play', methods=['GET'])
def play():
    user_input = request.args.get('text')
    if not user_input:
        return jsonify({'error': 'Missing "text" parameter'}), 400

    try:
        play_token_number(user_input)
        return jsonify({'status': 'played', 'input': user_input})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='192.168.1.251', port=5000, debug=True)
