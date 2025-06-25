```markdown
# MultiLangVoice: Token Announcement System

MultiLangVoice is a Python-based system designed to convert numerical and text-based inputs into spoken audio announcements. Its primary function is to serve as a token announcement system, where a phrase like "Token Number 2150" is converted into a sequence of audio files played in order, using a pre-recorded Gujarati voice.

The system is built in two main stages:
1.  **Audio Generation**: Scripts that use Google Text-to-Speech (gTTS) to generate `.wav` audio files for numbers and specific words (e.g., "hundred," "thousand") in Gujarati.
2.  **Audio Playback**: Application logic that takes a number, decomposes it into a sequence of playable parts, and then plays the corresponding audio files. This is provided as a command-line script and a Flask-based web API.

## Prerequisites

- Python 3.x
- `Flask`
- `playsound`
- `gTTS`
- `pydub`

## Installation

1.  Clone the repository or download the source files.
2.  Install the required Python packages:
    ```bash
    pip install Flask playsound gtts pydub
    ```

## Setup: Generating Audio Files

Before you can play any announcements, you must first generate the required `.wav` files. The system expects these files to be in an `audio/` directory.

1.  Navigate to the `generateAudios` directory:
    ```bash
    cd MultiLangVoice/generateAudios
    ```

2.  Run the generation scripts. This will create an `audio` directory inside `MultiLangVoice` and populate it with the necessary sound files.
    ```bash
    python numbers.py
    python words.py
    ```
    * `numbers.py` creates `1.wav` through `99.wav`.
    * `words.py` creates `100.wav`, `200.wav`, ..., `1000.wav`.

## How to Use

### 1. Command-Line Usage (`call.py`)

The `call.py` script is a simple way to test announcements locally.

1.  **Manually add prefix audio files**: The script can announce prefixes like "token number". You must manually create audio files like `token.wav` and `number.wav` and place them in the `audio/` directory.
2.  Edit the `user_input` variable inside `call.py` to your desired announcement text.
    ```python
    # Inside call.py
    if __name__ == '__main__':
        user_input = 'token number 2150' # Change this line
        play_token_number(user_input)
    ```
3.  Run the script from the `MultiLangVoice/` directory:
    ```bash
    python call.py
    ```
    The audio will play through your system's speakers.

### 2. API Usage (`api.py`)

The `api.py` script deploys the system as a web service, allowing you to trigger announcements via HTTP requests.

1.  From the `MultiLangVoice/` directory, run the Flask application:
    ```bash
    python api.py
    ```
    The server will start, listening on `http://192.168.1.251:5000` by default.

2.  From any device on the same network, make a GET request to the `/play` endpoint with a `text` parameter.
    * **Using a Browser**: Navigate to `http://192.168.1.251:5000/play?text=token%20number%202150`
    * **Using cURL**:
        ```bash
        curl "[http://192.168.1.251:5000/play?text=token%20number%202150](http://192.168.1.251:5000/play?text=token%20number%202150)"
        ```
    The audio will be played on the machine where the `api.py` script is running. The API will respond with a JSON confirming the action.

## Core Logic and Components

### `get_audio_sequence(num)`
This is the core function of the project. It takes an integer (e.g., 2150) and decomposes it into a list of numbers corresponding to the audio files that need to be played (`[2, 1000, 1, 100, 50]`). This allows the system to construct the announcement dynamically.

### Component Scripts
* **`generateAudios/numbers.py`**: Generates `.wav` files for numbers 1-99 in Gujarati.
* **`generateAudios/words.py`**: Generates `.wav` files for round numbers (100, 200...1000) in Gujarati.
* **`number.py`**: A simple test script to demonstrate and debug the number decomposition and playback logic for a single number.
* **`call.py`**: Provides a command-line interface to parse a full string (with text and numbers) and play the corresponding announcement.
* **`api.py`**: Wraps the functionality of `call.py` into a Flask web server, exposing it through a `/play` endpoint.
````
