import socket
import wave

server_ip = "0.0.0.0"
server_port = 5000
buffer_size = 1024

# Set up socket to receive data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, server_port))
    s.listen(1)
    print("Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # Save received audio data to a WAV file
        with wave.open("audio_received.wav", "wb") as wf:
            wf.setnchannels(1)  # Mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(44100)  # Sample rate
            print("Receiving audio...")
            while True:
                data = conn.recv(buffer_size)
                if not data:
                    break
                wf.writeframes(data)
        print("Audio reception completed.")