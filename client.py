# Program Name: client.py (Program A)
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment4
# Due Date: 3/24/2024
# Purpose: This program collects the input of the user which will then be sent over a socket to program B.

# Program A
import socket

def client():
    host = '127.0.0.1'  # IP
    port = 63333  #

    # socket used to connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("[CLIENT] Enter a message: ")  # inputted string
        s.sendall(message.encode())  # send message
        data = s.recv(1024)  # receive response
        print(f"[CLIENT] Server replied: {data.decode()}")

if __name__ == "__main__":
    client()
