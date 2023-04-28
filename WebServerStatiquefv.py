"""
 Implements a simple HTTP/1.0 Server

"""

import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

dict={"/":"index.html","/index.html":'index.html',
      "/index/page2.html":"page2.html",
      "/page2.html":"page2.html",
      "/index/page3.html":"page3.html",
      "/page3.html":"page3.html",
      "/index/page4.html":"page4.html",
      "/page4.html":"page4.html"}



while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Get the content of htdocs/index.html
    headers = request.split('\n')
    print(headers)
    filename = headers[0].split()[1]


    # Send HTTP response
    try:
        filename = dict[filename]
        fin = open(filename)
        content = fin.read()
        fin.close()
        response = 'HTTP/1.0 200 OK\n\n' + content
    except Exception :
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found :('



    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()