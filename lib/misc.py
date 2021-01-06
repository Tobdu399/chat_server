import tkinter
import tkinter.font as font
import socket
from tkinter import messagebox
import threading
import traceback
from pathlib import Path
from datetime import datetime

display = tkinter.Tk()

errors = []

log_messages = []

background_color = "#313140"
foreground_color = "#DCDCDC"
button_color = "#3A64C9"

ip = socket.gethostbyname(socket.gethostname())

smallFont = font.Font(display, family="Helvetica", size=9)
normalFont = font.Font(display, family="Helvetica", size=11)

hosting = False
connected = False

date = str(datetime.now().strftime("[%d.%m.%Y][%H.%M.%S]"))
path = str(Path(__file__).resolve().parent.parent)


def log_errors():
    if len(errors) > 0:
        Path(f"{path}/logs/").mkdir(parents=True, exist_ok=True)
        error_log = open(f"{path}/logs/{date}.log", "w")

        error_log.write(f"{date}.log\n[day.month.year][hours.minutes.seconds]\n")

        for error in errors:
            error_log.write(f"\n[{'='*30}]\n\n{str(error)}")
        error_log.close()


def update_ip():
    global ip

    ip = socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    exit()
