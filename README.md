# RealTime-Audio-Transcription-Pi
This project enables real-time audio streaming from one device to another, where the audio is processed and transcribed into text. Using Python, socket programming, PyAudio, and the SpeechRecognition library, it captures live audio on device 1 and sends it to another device over a network, and performs speech-to-text transcription.

## Dependencies
Portaudio needs to be installed on both devices
Debian Distributions
```
sudo apt-get install portaudio19-dev
```

MacOS
```
brew install portaudio
```

Windows

```
https://www.portaudio.com/download.html
```

Then, On both devices, run

```
pip install -r requirements.txt
```

module installation will fail if Portaudio is not installed

## Procedure
On the Recieving Device first run
```
python audio_receiver.py
```

On the Sending Device run
```
python send_audio.py
```

Lastly, on the Recieving Device run
```
python audio_transcriber.py
```