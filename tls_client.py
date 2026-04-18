import socket
import ssl

SERVER_IP = "10.0.0.67"
PORT = 8443

context = ssl.create_default_context()
context.check_hostgit add .name = False
context.verify_mode = ssl.CERT_NONE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with context.wrap_socket(client_socket) as tls_client:
    tls_client.connect((SERVER_IP, PORT))
    print("[CLIENT] Securely connected to server.")

    message = input("Enter message: ")
    tls_client.send(message.encode())

    reply = tls_client.recv(1024).decode()
    print(f"[CLIENT] Reply from server: {reply}")

print("[CLIENT] Connection closed.")