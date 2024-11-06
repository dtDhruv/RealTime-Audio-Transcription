import socket
import pyaudio

server_ip = "IP ADDRESS"  # Replace with the receiving device's IP
server_port = 5000
buffer_size = 1024

# Audio setup
audio_format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = buffer_size

p = pyaudio.PyAudio()
stream = p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

# Socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_ip, server_port))
    print("Streaming audio to Raspberry Pi...")
    try:
        while True:
            data = stream.read(chunk)
            s.sendall(data)
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Audio stream ended.")
