import tkinter
import tkinter.font as font
from tkinter import messagebox

from . import entry
from . import button
from . import misc
from . import client
from . import scrollableframe as sframe
from . import checkbox
from . import server

padding = 10
display = tkinter.Tk()

display.geometry("500x400")
display.resizable(False, False)
display.title("Server")
display.config(bg=misc.background_color)

smallFont = font.Font(family="Helvetica", size=8)
normalFont = font.Font(family="Helvetica", size=11)

# Buttons
button.buttons["connect"] = button.Button(display, padding, padding + 85,
                                          70, 30, "Connect",
                                          lambda: client.connect(entry.entries["username"], entry.entries["port"], entry.entries["ip"]),
                                          "#09e378", normalFont)

button.buttons["host"] = button.Button(display, padding + 200 - 70, padding + 85,
                                       70, 30, "Host",
                                       lambda: server.host(entry.entries["port"]),
                                       "#09e378", normalFont)

button.buttons["send"] = button.Button(display, 500 - padding * 2 - 49, 185,
                                       60, 21, "Send",
                                       lambda: client.send_msg(entry.entries["message"]),
                                       "#09e378", smallFont)

# Entries
entry.entries["username"] = entry.InputField(display, padding, padding, 200, 20, "Username")
entry.entries["port"] = entry.InputField(display, padding, padding + 25, 200, 20, "Port (i.e. 1024)")
entry.entries["ip"] = entry.InputField(display, padding, padding + 50, 200, 20, "IP (i.e. 192.168.0.0")
entry.entries["message"] = entry.InputField(display, padding, 185, 500 - padding * 2 - 65, 20, "Your message...")

# Scrollable entries
log_messages = sframe.ScrollableFrame(display)

# Checkboxes
auto_scroll = tkinter.IntVar(value=1)
checkbox.checkboxes.append(checkbox.Checkbox(display, padding, 155, auto_scroll, "Enable auto-scroll"))


def update_log():
    for log in misc.log_messages:
        log = tkinter.Label(log_messages.scrollable_frame, padx=5, pady=0, bg="white", anchor='w', text=log)
        log.config(width=67)
        log.pack()

    misc.log_messages = []

    if auto_scroll.get() == 1:
        log_messages.canvas.yview_moveto(1)

    display.after(100, update_log)


def on_closing():
    if misc.hosting:
        if messagebox.askyesno("You are the Host", "You are Hosting a server! Are you sure you want to quit?"):
            client.disconnect()
            display.destroy()
    elif misc.connected:
        if messagebox.askyesno("You are connected", "You are connected to a server! Are you sure you want to quit?"):
            client.disconnect()
            display.destroy()
    else:
        display.destroy()


def main():
    for btn in button.buttons:
        button.buttons[btn].show()

    for ent in entry.entries:
        entry.entries[ent].show()

    for cbox in checkbox.checkboxes:
        cbox.show()

    display.after(100, update_log)

    log_messages.pack_propagate(0)
    log_messages.place(x=padding, y=210, width=500 - padding * 2, height=180)
    log_messages.style()

    display.protocol("WM_DELETE_WINDOW", on_closing)
    display.mainloop()
