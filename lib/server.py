from lib import misc
from lib.misc import display

clients = {}


def listener(client):
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
        if not misc.connected:
            if PORT != port.placeholder and PORT != "":
                try:
                    PORT = int(PORT)

                    server_thread = misc.threading.Thread(target=start_server, args=(PORT,))
                    server_thread.daemon = True
                    server_thread.start()
                except ValueError:
                    misc.log_messages.append("[SERVER] Invalid port")
            else:
                misc.log_messages.append("[SERVER] Invalid port")
        else:
            misc.log_messages.append("[SERVER] Can't start hosting! You are already connected to a server")
    else:
        misc.log_messages.append("[SERVER] You are already hosting a server!")


def start_server(port):
    HOST = misc.ip
    PORT = port

    # listen for new TCP connections
    s = misc.socket.socket(misc.socket.AF_INET, misc.socket.SOCK_STREAM)
    s.setsockopt(misc.socket.SOL_SOCKET, misc.socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    misc.log_messages.append(f"[SERVER] Server listening at port {PORT}")
    misc.update_ip()
    misc.log_messages.append(f"[SERVER] Host IP address: {misc.ip}")
    misc.hosting = True

    s.listen()

    while True:
        conn, addr = s.accept()
        clients[conn] = misc.threading.Thread(target=listener, args=(conn,)).start()


if __name__ == "__main__":
    exit()
