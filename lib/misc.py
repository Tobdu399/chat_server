import socket

errors = []

log_messages = []
background_color = "powderblue"
ip = socket.gethostbyname(socket.gethostname())

hosting = False
connected = False


def update_ip():
    global ip

    ip = socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    exit()
