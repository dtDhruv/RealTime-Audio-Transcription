import speech_recognition as sr
import time
import os

audio_file = "audio_received.wav"

def transcribe_audio():
    recognizer = sr.Recognizer()
    while True:
        if os.path.exists(audio_file):
            try:
                with sr.AudioFile(audio_file) as source:
                    audio_data = recognizer.record(source)
                    text = recognizer.recognize_google(audio_data)
                    os.system("clear")
                    print("Transcription:", text)
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        time.sleep(1)

if __name__ == "__main__":
    transcribe_audio()