import socket
# from rich.console import Console
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore, Back, Style


# connecting animation


def start_server():
    # automatically get the IP address of the server
    host = socket.gethostbyname(socket.gethostname())
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}...")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(Fore.GREEN + f" Connection established with {client_address}")

            handle_client(client_socket)

        except KeyboardInterrupt:
            print(Fore.RED + "\nServer shutting down.")
            break

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()

            if not data: # if the client disconnects
                break
            
            if data == 'B':
                decimal_input = int(client_socket.recv(1024).decode()) # receive the decimal input from the client
                binary_output = bin(decimal_input)[2:] # convert the decimal input to binary. 
                client_socket.send(str(binary_output).encode())

            elif data == 'H':
                decimal_input = int(client_socket.recv(1024).decode())
                hex_output = hex(decimal_input)[2:]
                client_socket.send(str(hex_output).encode())

            elif data == 'Q':
                print(Fore.RED + "Client disconnected.")
                break

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_server()
