# Import the necessary libraries
from transformers import pipeline

# Initialize the text classification model with a pre-trained model
model_text_emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Initialize the audio classification model with a pre-trained SER model
model_speech_emotion = pipeline("audio-classification", model="aherzberg/ser_model_fixed_label")

# Initialize the automatic speech recognition model with a pre-trained model that is capable of converting speech to text
model_voice2text = pipeline("automatic-speech-recognition", model="openai/whisper-tiny.en")

# A function that uses the initialized text classification model to predict the emotion of a given text input
def infere_text_emotion(text):
    return model_text_emotion(text)[0]["label"].capitalize()

# A function that uses the initialized audio classification model to predict the emotion of a given speech input
def infere_speech_emotion(text):
    return model_speech_emotion(text)[0]["label"]

# A function that uses the initialized automatic speech recognition model to convert speech (as an audio file) to text
def infere_text_to_voice(audio_file):
    return model_voice2text(audio_file)["text"]