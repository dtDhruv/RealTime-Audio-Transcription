# RealTime-Audio-Transcription-Pi
This project enables real-time audio streaming from a laptop to a Raspberry Pi, where the audio is processed and transcribed into text. Using Python, socket programming, PyAudio, and the SpeechRecognition library, it captures live audio on the laptop, sends it to the Raspberry Pi over a network, and performs speech-to-text transcription on the Pi.

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