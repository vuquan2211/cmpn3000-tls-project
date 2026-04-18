import socket
import ssl

HOST = "0.0.0.0"
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print("Server listening...")

with context.wrap_socket(sock, server_side=True) as ssock:
    conn, addr = ssock.accept()
    print("Connected from", addr)

    data = conn.recv(1024).decode()
    print("Received:", data)

    conn.send("Hello from TLS server".encode())
    conn.close()