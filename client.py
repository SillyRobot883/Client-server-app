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
                print("current user input: " + str(user_input))
                print("Length of user input: " + str(len(user_input)))
                
                

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
                    else:
                        print(Fore.RED + "Length ain't 2")
                        print(Style.RESET_ALL)                    
                        continue 
                else:
                    # for debugging 
                    print("OPTION: " + str(type(user_input[0])))
                    print("Decimal Number: " + user_input[1])
                    # Check for 400 The number is missing: Missing the number
                    if not user_input[1].isdigit():
                            print(Fore.RED + "Error: missing the number")
                            print(Style.RESET_ALL) 
                    
                    # Check for 300 Bad Request: Missing B or H
        
                    if not (user_input[0] == 'B' or user_input[0] == 'H'):
                        print(Fore.RED + "Error: Missing B or H")
                        print(Style.RESET_ALL) 
                    else:
                         print("we good!")
                        # conversion here
                
               
                # else:
                #     print(Fore.GREEN + "Everything is alright!")
                #     print("OPTION: " + user_input[0])
                #     print("Decimal Number: " + user_input[1])
                
                # Validate the input
                # if user_input == 'Q':
                #     print(Fore.RED + "Quitting...")
                #     print(Style.RESET_ALL)
                #     client_socket.send(user_input.encode())
                #     break
                    
                # if user_input == 'B' or user_input == 'H' and user_input: # if the input does not match the pattern
                #     print(Fore.GREEN + 'Valid choice')
                    # print(Style.RESET_ALL)


                #     # deal with the input 
                #     client_socket.send(user_input.encode())
                #     if user_input[0] == 'B': # [0] is the first arg, which is the choice
                #         decimal_input = int(user_input.split()[1]) # [1] is the second arg, which is the number to convert
                #         client_socket.send(str(decimal_input).encode()) # send the decimal input to the server
                #         binary_output = client_socket.recv(1024).decode() # receive the binary output from the server
                #         print(Fore.LIGHTGREEN_EX + f"Binary: {binary_output}") # print the binary output
                #     if user_input[0] == 'H':
                #         decimal_input = int(user_input.split()[1])
                #         client_socket.send(str(decimal_input).encode())
                #         hex_output = client_socket.recv(1024).decode()
                #         print(Fore.LIGHTBLUE_EX + f"Hexadecimal: {hex_output}")
                    
                    
                # else: 
                #     print(Fore.RED + "Invalid choice. Please try again.") 
                #     # stop colorama
                #     print(Style.RESET_ALL)



        except ConnectionRefusedError:  # if the server is down
            print(Fore.RED + "[*] Server is down. Try again.")

        finally:
            client_socket.close()

    if __name__ == "__main__":
        start_client()

except KeyboardInterrupt:  # handles Ctrl+C to quit the program
        print(Fore.RED + "[*] Quitting...")
except Exception as e:
    print(Fore.RED + f"Error: {e}")
