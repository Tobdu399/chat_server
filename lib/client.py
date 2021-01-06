from lib import misc
from lib.misc import threading, traceback, datetime, socket, display

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

USERNAME = ""
PORT = ""
IP = ""


def connect(username, port, ip):
    global USERNAME
    global PORT
    global IP

    USERNAME = username.get()
    PORT = port.get()
    IP = ip.get()

    if not misc.connected:
        if USERNAME != username.placeholder and " " not in USERNAME and USERNAME != "":
            if PORT != port.placeholder and " " not in PORT and PORT != "":
                try:
                    PORT = int(PORT)

                    if IP != ip.placeholder and " " not in IP and IP != "":
                        main()
                    else:
                        misc.log_messages.append("[INFO] Invalid IP")

                except ValueError:
                    error = traceback.format_exc()
                    misc.errors.append(error)

                    misc.log_messages.append("[INFO] Invalid port")
            else:
                misc.log_messages.append("[INFO] Invalid port")
        else:
            misc.log_messages.append("[INFO] Invalid username")
    else:
        misc.log_messages.append("[INFO] You are already connected to a server")


def disconnect():
    try:
        s.send(f"@{USERNAME} left".encode())
        s.close()
    except OSError:
        error = traceback.format_exc()
        misc.errors.append(error)

        misc.log_messages.append("[ERROR] An unexpected error occurred!")
    finally:
        misc.hosting = False
        misc.connected = False
        display.destroy()


def send_msg(entry):  # Give the entry where the message will be grabbed from
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")

    message_input = entry.get()

    try:
        if message_input != "" and message_input != entry.placeholder:
            entry.delete('0', "end")  # Clear the entry box after sending the message
            message = f"[{current_time}] @{USERNAME}: {message_input}"
            s.sendall(message.encode())
    except OSError:
        error = traceback.format_exc()
        misc.errors.append(error)

        misc.log_messages.append("[INFO] You must be connected to a server to send messages\n")


def receive_msg():
    while misc.connected:
        try:
            from_server = str(s.recv(1024))[2:-1]
            misc.log_messages.append(from_server)
        except(ConnectionResetError, ConnectionAbortedError, OSError):
            error = traceback.format_exc()
            misc.errors.append(error)

            misc.log_messages.append("\n[CONNECTION ERROR] Connection to the server lost!\n")
            misc.connected = False
            misc.hosting = False


def main():
    receive_msg_thread = threading.Thread(target=receive_msg)
    receive_msg_thread.daemon = True

    try:
        try:
            s.connect((IP, PORT))
            misc.log_messages.append(f"[SERVER] Connection established\n")
            misc.connected = True
            receive_msg_thread.start()

            try:
                s.send(f"@{USERNAME} joined!".encode())
            except OSError:
                error = traceback.format_exc()
                misc.errors.append(error)

                misc.log_messages.append("[ERROR] A Connection error occurred possibly due to an invalid IP")
                misc.connected = False

        except socket.gaierror:
            error = traceback.format_exc()
            misc.errors.append(error)

            misc.log_messages.append("[CONNECTION ERROR] Invalid IP")
            misc.connected = False

    except ConnectionRefusedError:
        error = traceback.format_exc()
        misc.errors.append(error)

        misc.log_messages.append(f"[CONNECTION ERROR] Connection to port {PORT} failed!\n")
        misc.connected = False


if __name__ == "__main__":
    exit()
