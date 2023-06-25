import sys
import socket
import logging
import time

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.18.0.5', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()

if __name__=='__main__':
    total_requests = 0  # Add a counter for total requests
    start_time = time.time()  # Get the starting time
    while time.time() - start_time < 10:  # Run the loop for 10 seconds
        kirim_data()
        total_requests += 1  # Increment the counter for each request
    logging.warning(f"Total requests sent: {total_requests}")
