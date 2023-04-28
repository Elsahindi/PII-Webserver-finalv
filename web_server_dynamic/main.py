
import socket
from cgitb import html

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8090

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Get the content of htdocs/index.html
    headers = request.split('\n')
    filename = headers[0].split()[1]

    try:


        fin = open(r'C:\Users\Lenovo\Desktop\Nouveau\Notresite.html')

        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'


    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()