import socket
import threading #server side code.......

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client: {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)

clients = []

print("Server started...")

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr} has been established!")
    clients.append(client_socket)

    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()