import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def start_conversation():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
        server_conn.connect((HOST, PORT))
        _poll(server_conn)


def _poll(server_conn):
    while True:
        data = server_conn.recv(1024)
        bot_response = '[Bot] <-' + str(data) + '\n'
        user_input = input(bot_response)
        print(f'[You] -> {user_input}')
        server_conn.sendall(user_input.encode('utf-8'))


if __name__ == '__main__':
    start_conversation()
