import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

messages = ["I am Client.", "Nice to meet you!"]
for msg in messages:
    client_socket.send(msg.encode())
    print(f"Client: {msg}")
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

client_socket.close()
