# TLS Client-Server Application

This project demonstrates a simple client-server application using TLS over TCP in Python.

## Overview

- A TLS server is created using a self-signed certificate.
- A TLS client connects securely using Python’s SSL module.
- Messages are exchanged between the client and server.
- Wireshark is used to verify that the data is encrypted.

## Files

- `tls_server.py` – TLS server implementation  
- `tls_client.py` – TLS client implementation  
- `server.crt` – Self-signed certificate  
- `server.key` – Private key  
- `generate_cert.py` – Script to generate certificate  

## How to Run

### 1. Start the server
```bash
python tls_server.py
