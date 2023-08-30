import socket

def ack_servidor(server_sinc):
    socket_sinc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_sinc.bind (server_sinc)
    socket_sinc.listen(1)
    conexion, direccion = socket_sinc.accept()

    mensaje_recibido = conexion.recv(1024)
    if mensaje_recibido.decode() == 'ACK-SYN':
        print('Sincronizacion correcta en', direccion)
        # Enviar ACK al cliente
        conexion.sendall(b'ACK OK')
        socket_sinc.close()
        return True
    else:
        socket_sinc.close()
        return False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0'

port_stream = 12345

port_sinc = 54321

sock.bind((ip,port_stream))

sock.listen(1)

server_sinc=((ip,port_sinc))

print(f"Servidor escuchando en {ip}:{port_stream}")
connection, client = sock.accept()

print (client, 'Comunicacion establecida')

while True:
    if (ack_servidor(server_sinc)) == True: 
        # Recibir datos desde el cliente
        data = connection.recv(1024)
    
        print(f"Mensaje recibido de {client}: {data.decode()}")

        # Responder al cliente
        response = "Mensaje recibido correctamente"
        connection.sendto(response.encode(), client)
        message = input("Ingrese un mensaje: ")
        connection.sendto(message.encode(), client)
        data = connection.recv(1024)
        print('Cliente:', data.decode())
    else:
            print(f"Se perdió la comunicacion con el servidor")
            connection.close()