from lib.misc import display, tkinter, messagebox, smallFont, normalFont, foreground_color
from lib import entry, button, misc, client, checkbox, server
from lib import scrollableframe as sframe

padding = 10

display.geometry("500x400")
display.resizable(False, False)
display.title("Python Chat Server")
display.config(bg=misc.background_color)

# Buttons
button.buttons["connect"] = button.Button(display, padding, padding + 87,
                                          70, 30, "Connect",
                                          lambda: client.connect(entry.entries["username"], entry.entries["port"],
                                                                 entry.entries["ip"]), normalFont)

button.buttons["host"] = button.Button(display, padding + 200 - 70, padding + 87,
                                       70, 30, "Host",
                                       lambda: server.host(entry.entries["port"]), normalFont)

button.buttons["send"] = button.Button(display, 500 - padding * 2 - 52, padding + 172,
                                       62, 25, "Send",
                                       lambda: client.send_msg(entry.entries["message"]), smallFont)

# Entries
entry.entries["username"] = entry.InputField(display, padding, padding, 200, 25, "Username")
entry.entries["port"] = entry.InputField(display, padding, padding + 28, 200, 25, "Port (i.e. 1024)")
entry.entries["ip"] = entry.InputField(display, padding, padding + 56, 200, 25, "IP (i.e. 192.168.0.0")
entry.entries["message"] = entry.InputField(display, padding, padding + 172, 500 - padding * 2 - 65, 25, "Your message...")

# Scrollable entries
msg_display = sframe.ScrollableFrame(display)

# Checkboxes
auto_scroll = tkinter.IntVar(value=1)
checkbox.checkboxes.append(checkbox.Checkbox(display, padding, 155, auto_scroll, "Enable auto-scroll"))


def update_log():
    for log in misc.log_messages:
        log = tkinter.Label(msg_display.scrollable_frame, padx=5, pady=0,
                            bg=foreground_color, anchor='w', text=log, font=smallFont)
        log.config(width=67)
        log.pack()

    misc.log_messages = []

    if auto_scroll.get() == 1:
        msg_display.canvas.yview_moveto(1)

    display.after(100, update_log)


def on_closing():
    if misc.hosting:
        if messagebox.askyesno("You are the Host", "You are Hosting a server! Are you sure you want to quit?"):
            client.disconnect()
    elif misc.connected:
        if messagebox.askyesno("You are connected", "You are connected to a server! Are you sure you want to quit?"):
            client.disconnect()
    else:
        client.disconnect()


def main():
    for btn in button.buttons:
        button.buttons[btn].show()

    for ent in entry.entries:
        entry.entries[ent].show()

    for cbox in checkbox.checkboxes:
        cbox.show()

    display.after(100, update_log)

    msg_display.pack_propagate(0)
    msg_display.place(x=padding, y=210, width=500 - padding * 2, height=180)
    msg_display.style()

    display.protocol("WM_DELETE_WINDOW", on_closing)
    display.mainloop()


if __name__ == "__main__":
    exit()
