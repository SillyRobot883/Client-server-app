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
            option = client_socket.recv(1024).decode() # receive option from client
            decimal_input = client_socket.recv(4096).decode() # receive the decimal input from the client

            print("Option: " + option)
            print("Number: " + str(decimal_input))
            if not option: # if the client disconnects
                break
            
            if option == 'B':
                binary_output = bin(int(decimal_input))[2:] # convert the decimal input to binary. 
                client_socket.send(str(binary_output).encode())

            if option == 'H':
                hex_output = hex(int(decimal_input))[2:]
                client_socket.send(str(hex_output).encode()) # 

            if option == 'Q':
                print(Fore.RED + "Client disconnected.")
                break

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_server()
