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

                user_input = input("Enter conversion option and number (e.g., B 50 or H 12): ").upper()
                # pattern = re.compile(r'^[BH] \d+$')


                # error checking 
                user_input = user_input.split() # split option and number
                # temp for debugging
                # print("current user input: " + str(user_input))
                # print("Length of user input: " + str(len(user_input)))
                
                if len(user_input) != 2: # first, check if that there is exactly 2 arguments
                    # Check for 500 Request Is Empty: Missing both the letter and number
                    if len(user_input) == 0: 
                        print(Fore.RED + "Error: Missing both the letter and number")
                        print(Style.RESET_ALL)
                        continue
                     # handle quitting using 'Q'
                    if user_input[0] == 'Q':
                        print(Fore.RED + "Quitting...")
                        print(Style.RESET_ALL)
                        client_socket.send(user_input[0].encode()) # send input to server
                        break
                    # print error message for length error
                    else:
                        print(Fore.RED + "Length is not 2, try again")
                        print(Style.RESET_ALL)                    
                        continue 
                else:
                    # for debugging: TO DELETE
                    # print("OPTION: " + str(type(user_input[0])))
                    # print("Decimal Number: " + user_input[1])
                    # Check for 400 The number is missing: Missing the number
                    if not user_input[1].isdigit():
                            print(Fore.RED + "Error: missing the number")
                            print(Style.RESET_ALL) 
                    
                    # Check for 300 Bad Request: Missing B or H
        
                    elif not (user_input[0] == 'B' or user_input[0] == 'H'):
                        print(Fore.RED + "Error: Missing B or H")
                        print(Style.RESET_ALL) 
                    else:
                        # conversion here
                        # deal with the input 
                        decimal_input = int(user_input[1]) # convert number from str to int
                        client_socket.send(str(user_input[0]).encode()) # send option 
                        client_socket.send(str(decimal_input).encode()) # send decimal
                        # binary conversion 
                        if user_input[0] == 'B': # [0] is the first arg, which is the choice
                            binary_output = client_socket.recv(1024).decode() # receive the binary output from the server
                            print(Fore.LIGHTGREEN_EX + f"Binary: {binary_output}") # print the binary output
                            print(Style.RESET_ALL)
                        # hexadecimal conversion
                        if user_input[0] == 'H':
                            hex_output = client_socket.recv(4096).decode()
                            print(Fore.LIGHTBLUE_EX + f"Hexadecimal: {hex_output}")
                            print(Style.RESET_ALL)


        except ConnectionRefusedError:  # if the server is down
            print(Fore.RED + "[*] Server is down. Try again.")

        finally:
            client_socket.close()

    if __name__ == "__main__":
        start_client()

except KeyboardInterrupt:  # handles Ctrl+C to quit the program
        print(Fore.RED + "[*] Quitting...")
except ConnectionResetError:
        print(Fore.RED + "[*] Server has shutdown...")
except Exception as e:
    print(Fore.RED + f"[*] Error: {e}")

