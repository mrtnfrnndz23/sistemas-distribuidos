import socket

# Configuración del servidor
server_ip = "0.0.0.0"  # Escucha en todas las interfaces de red
server_port = 12345

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"Servidor escuchando en {server_ip}:{server_port}")

while True:
    # Recibir datos desde el cliente
    data, client_address = server_socket.recvfrom(1024)
    print(f"Mensaje recibido de {client_address}: {data.decode()}")

    # Responder al cliente
    response = "Mensaje recibido correctamente"
    server_socket.sendto(response.encode(), client_address)
