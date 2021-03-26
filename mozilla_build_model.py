from TTS/TTS/tts/datasets/preprocess.py import load_meta_data

in_data = {'name': 'ljspeech',
        'path': 'LJSpeech/LJSpeech1.1',
        'meta_file_val': None,
        'meta_file_eval': None}

load_meta_data()