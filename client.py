import socket
from termcolor import colored
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import re

# TITLE
custom_fig = Figlet(font="small", width=300)
print(custom_fig.renderText("Client-Server Application"))

try:
    def start_client():
        host = socket.gethostbyname(socket.gethostname())
        port = 12345

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # OPTIONS
            while True:
                print("\nOptions:")
                print("B: Convert decimal to binary")
                print("H: Convert decimal to hexadecimal")
                print("Q: Quit")
                print("Example: B 50")

                user_input = input("Enter your choice: ").upper()
                pattern = re.compile(r'^[BH] \d+$')

                # Validate the input
                if user_input == 'Q':
                    print(Fore.RED + "Quitting...")
                    client_socket.send(user_input.encode())
                    break
                if not pattern.match(user_input): # if the input does not match the pattern
                    print(Fore.RED + "Invalid choice. Please try again.") 
                    # stop colorama
                    print(Style.RESET_ALL)
                else: 
                    print(Fore.GREEN + 'Valid choice')
                    print(Style.RESET_ALL)
                    # deal with the input 
                    client_socket.send(user_input.encode())
                    if user_input[0] == 'B': # [0] is the first arg, which is the choice
                        decimal_input = int(user_input.split()[1]) # [1] is the second arg, which is the number to convert
                        client_socket.send(str(decimal_input).encode()) # send the decimal input to the server
                        binary_output = client_socket.recv(1024).decode() # receive the binary output from the server
                        print(Fore.LIGHTGREEN_EX + f"Binary: {binary_output}") # print the binary output
                    if user_input[0] == 'H':
                        decimal_input = int(user_input.split()[1])
                        client_socket.send(str(decimal_input).encode())
                        hex_output = client_socket.recv(1024).decode()
                        print(Fore.LIGHTBLUE_EX + f"Hexadecimal: {hex_output}")



        except ConnectionRefusedError:  # if the server is down
            print(Fore.RED + "[*] Server is down. Try again.")

        finally:
            client_socket.close()

    if __name__ == "__main__":
        start_client()

except KeyboardInterrupt:  # handles Ctrl+C to quit the program
        print(Fore.RED + "[*] Quitting...")
