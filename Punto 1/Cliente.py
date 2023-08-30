import socket
import time

# Configuración del cliente
server_ip = "localhost"
server_port = 12345

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(10)  # Establecer un tiempo de espera de 10 segundos

while True:
    try:
        # Solicitar al usuario ingresar un mensaje
        message = input("Ingrese un mensaje: ")

        # Enviar el mensaje al servidor
        client_socket.sendto(message.encode(), (server_ip, server_port))

        # Recibir la respuesta del servidor
        response, server_address = client_socket.recvfrom(1024)
        print(f"Respuesta del servidor: {response.decode()}")

    except socket.timeout:
        print("No se pudo efectuar la comunicación con el servidor")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(1)  # Esperar un segundo antes de volver a solicitar un mensaje
