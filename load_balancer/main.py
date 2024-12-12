import sys
import os
from itertools import cycle
from socket import socket, AF_INET, SOCK_STREAM


def initialize_servers():
	num_servers = int(os.environ['SERVER_COUNT'])
	servers = [f'se-lab6-backend-{i + 1}' for i in range(num_servers)]
	print(num_servers, 'Available servers:', servers)
	return cycle(servers)


def handle_socket():
	with socket(AF_INET, SOCK_STREAM) as sock:
		sock.bind((host, port))
		sock.listen()
		print(f'Listening on {host}:{port}')

		while True:
			conn, addr = sock.accept()
			print(f'Received request from {addr[0]}:{addr[1]}')
			with conn:
				while True:
					req = conn.recv(1024)
					if not req: break

					next_server = next(servers)
					print(f'Sending request from {addr[0]}:{addr[1]} to {next_server}:5000')
					with socket(AF_INET, SOCK_STREAM) as sock2:
						sock2.connect((next_server, 5000))
						sock2.send(req)
						while True:
							res = sock2.recv(1024)
							if not res: break
							conn.send(res)


if __name__ == "__main__":
	print('hello world')

	host = os.environ['LB_HOST']
	port = int(os.environ['LB_PORT'])
	servers = initialize_servers()
	handle_socket()
