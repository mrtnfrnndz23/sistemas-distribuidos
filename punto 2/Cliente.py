import socket
import time

def ack_cliente(ip,port_sinc):
    sinc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sinc_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sinc_socket.connect((ip,port_sinc))

    mensaje = b'ACK-SYN'
    sinc_socket.sendall(mensaje)

    ack = sinc_socket.recv(1024)
    if ack.decode() == 'ACK OK':
        print(f"Sincronizado en {ip}:{port_sinc}")
        sinc_socket.close()
        return True
    else:
        sinc_socket.close()
        return False


#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), específicamente IPv4. 
# El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP. 
# Asimismo, también puedes crear un socket IPv6 especificando el argumento del socket AF_INET6.

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'

port = 12345

port_sinc = 54321

sinc = False

server_address = ((ip,port))

print ("Conectando...")

stream_socket.connect(server_address)

while True:
    try:
        if (ack_cliente(ip,port_sinc)) == True:
            # Solicitar al usuario ingresar un mensaje
            message = input("Ingrese un mensaje: ")
        
            # Enviar el mensaje al servidor
            stream_socket.sendall(message.encode())

            # Recibir la respuesta del servidor
            response, server_address = stream_socket.recvfrom(1024)
            print(f"Respuesta del servidor: {response.decode()}")
            
            response, server_address = stream_socket.recvfrom(1024)
            recibido = "Mensaje recibido correctamente"
            stream_socket.sendall(recibido.encode())
            print(f"Servidor: {response.decode()}")

        else:
            print(f"Se perdió la comunicacion con el servidor")
            stream_socket.close()

    except socket.timeout:
        print("No se pudo efectuar la comunicación con el servidor")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(1)  # Esperar un segundo antes de volver a solicitar un mensaje