import socket
import threading
import misc

clients = {}


def listener(client, address):
    try:
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break

                for c in clients.keys():
                    if c != client:
                        c.sendall(data)

                client.send(data)
            except ConnectionResetError:
                clients.pop(client)
                break
    finally:
        client.close()


def host(port):
    PORT = port.get()

    if not misc.hosting:
        if PORT != port.placeholder and PORT != "":
            try:
                PORT = int(PORT)
                server_thread = threading.Thread(target=start_server, args=(PORT,))
                server_thread.daemon = True
                server_thread.start()
            except ValueError:
                misc.log_messages.append("[SERVER] Invalid port")
        else:
            misc.log_messages.append("[SERVER] Invalid port")
    else:
        misc.log_messages.append("[SERVER] You are already hosting a server!")


def start_server(port):
    HOST = misc.ip
    PORT = port

    # listen for new TCP connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    misc.log_messages.append(f"[SERVER] Server listening at port {PORT}...")
    misc.update_ip()
    misc.log_messages.append(f"[SERVER] Host IP address: {misc.ip}")
    misc.hosting = True

    s.listen()

    while True:
        conn, addr = s.accept()
        clients[conn] = threading.Thread(target=listener, args=(conn, addr)).start()
