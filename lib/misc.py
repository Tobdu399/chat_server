import socket

log_messages = []
background_color = "powderblue"
ip = socket.gethostbyname(socket.gethostname())

hosting = False
connected = False


def update_ip():
    global ip

    ip = socket.gethostbyname(socket.gethostname())
