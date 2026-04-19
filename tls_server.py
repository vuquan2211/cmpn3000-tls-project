import socket
import ssl


HOST = "0.0.0.0"
PORT = 8443
CERT_FILE = "server.crt"
KEY_FILE = "server.key"


def create_server_socket() -> ssl.SSLSocket:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[SERVER] Listening on {HOST}:{PORT}")
    return context.wrap_socket(server_socket, server_side=True)


def handle_client(conn: ssl.SSLSocket, addr) -> None:
    print(f"[SERVER] Connected from {addr}")

    data = conn.recv(1024)
    if not data:
        print("[SERVER] No data received.")
        return

    message = data.decode()
    print(f"[SERVER] Received: {message}")

    reply = "Hello from TLS server"
    conn.send(reply.encode())
    print("[SERVER] Reply sent.")


def main() -> None:
    server_socket = None
    conn = None

    try:
        server_socket = create_server_socket()
        conn, addr = server_socket.accept()
        handle_client(conn, addr)

    except FileNotFoundError:
        print("[SERVER] Certificate or key file not found.")
    except ssl.SSLError as e:
        print(f"[SERVER] SSL error: {e}")
    except OSError as e:
        print(f"[SERVER] Socket error: {e}")
    except Exception as e:
        print(f"[SERVER] Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
            print("[SERVER] Client connection closed.")
        if server_socket:
            server_socket.close()
            print("[SERVER] Server socket closed.")


if __name__ == "__main__":
    main()