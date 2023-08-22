import socket
import tkinter as tk
from tkinter import messagebox

class UDPClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente UDP")
        
        self.server_ip_label = tk.Label(root, text="IP del servidor:")
        self.server_ip_label.pack()
        
        self.server_ip_entry = tk.Entry(root)
        self.server_ip_entry.pack()
        
        self.message_label = tk.Label(root, text="Mensaje:")
        self.message_label.pack()
        
        self.message_entry = tk.Entry(root)
        self.message_entry.pack()
        
        self.send_button = tk.Button(root, text="Enviar", command=self.send_message)
        self.send_button.pack()

        # Configuración del cliente
        self.server_ip = ""
        self.server_port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(10)

    def send_message(self):
        self.server_ip = self.server_ip_entry.get()
        message = self.message_entry.get()

        try:
            self.client_socket.sendto(message.encode(), (self.server_ip, self.server_port))
            response, server_address = self.client_socket.recvfrom(1024)
            messagebox.showinfo("Respuesta", f"Respuesta del servidor: {response.decode()}")
        except socket.timeout:
            messagebox.showerror("Error", "No se pudo efectuar la comunicación con el servidor")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UDPClientGUI(root)
    root.mainloop()
