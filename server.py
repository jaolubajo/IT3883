# Program Name: server.py (Program B)
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment4
# Due Date: 3/24/2024
# Purpose: This program converts the user input from program A into uppercase and sends it back through the socket.

# Program B
import socket

def server():
    host = '127.0.0.1'  # local host
    port = 63333  # port number

    # create a socket for the host and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("[SERVER] Connecting...")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected to {addr}")
            data = conn.recv(1024)  # receive string from client
            if data:
                response = data.decode().upper()  # to uppercase
                conn.sendall(response.encode())  # response
                print(f"[SERVER]: {response}")

if __name__ == "__main__":
    server()

