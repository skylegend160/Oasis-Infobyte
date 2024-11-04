import socket        #client side server code
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            print("An error occurred!")
            client_socket.close()
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    message = input("")
    client.send(message.encode('utf-8'))