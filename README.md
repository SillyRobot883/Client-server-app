# CS330 Networking Project: TCP Client-Server Application

## Description

This repository contains the implementation of a simple TCP client-server application in Python. The client and server communicate over the network, allowing the client to send conversion requests to the server and receive the results.

## Project Overview

The goal of this project is to implement a TCP client and server that performs decimal-to-binary and decimal-to-hexadecimal conversions. The server runs in passive mode, waiting for a connection from the client. Once connected, the client can send conversion requests to the server, which processes the requests and returns the results.

## Project Components

### client.py

The client script establishes a connection to the server and provides a command line interface (CLI) for inputting conversion requests. The user can choose between converting a decimal number to binary or hexadecimal. The client performs error checking on user input and sends the request to the server. Upon receiving the server's response, the client displays the equivalent value or an error message.

### server.py

Similar to Netcat, the server script listens for incoming connections from clients. Once a connection is established, the server receives conversion requests from the client, processes them, and sends back the results. The server handles various error conditions and responds with appropriate messages.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/SillyRobot883/cs330-networking-project.git
2. Navigate to the project directory:
   ```bash
   cd cs330-networking-project
3. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
4. Run the server:
   ```bash
   python server.py
4. Open a new terminal window and run the client:
    ```bash
    python client.py
5. Follow the on-screen instructions to input conversion requests.

## Error Handling

The application handles several error conditions, including:
- **Server down:** If the server is not running, the client displays a message and exits gracefully.
- **Input errors:** The client checks for various input errors and provides descriptive error messages.
- **Server response errors:** The client displays error messages received from the server, indicating issues such as missing commands or numbers.




