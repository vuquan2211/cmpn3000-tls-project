import socket
import ssl


SERVER_IP = "10.0.0.67"
PORT = 8443


def create_tls_client() -> ssl.SSLSocket:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return context.wrap_socket(client_socket)


def main() -> None:
    tls_client = None

    try:
        tls_client = create_tls_client()
        tls_client.connect((SERVER_IP, PORT))
        print("[CLIENT] Securely connected to server.")

        message = input("Enter message: ").strip()
        if not message:
            print("[CLIENT] Empty message. Nothing was sent.")
            return

        tls_client.send(message.encode())
        reply = tls_client.recv(1024).decode()
        print(f"[CLIENT] Reply from server: {reply}")

    except ssl.SSLError as e:
        print(f"[CLIENT] SSL error: {e}")
    except OSError as e:
        print(f"[CLIENT] Connection error: {e}")
    except Exception as e:
        print(f"[CLIENT] Unexpected error: {e}")
    finally:
        if tls_client:
            tls_client.close()
            print("[CLIENT] Connection closed.")


if __name__ == "__main__":
    main()