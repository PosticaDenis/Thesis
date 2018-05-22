import socket
import tkinter as tk

UDP_IP = "192.168.1.5"
UDP_PORT = 5055
MESSAGE = "Hello, World!"

print ("UDP target IP: ", UDP_IP)
print ("UDP target port: ", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def key_input(event):
    print ("Key: ", event.char)
    key_press = event.char
    key_set = ['w', 's', 'a', 'd', 'q', 'e']

    if key_press.lower() in key_set:
        sock.sendto(key_press.lower().encode(), (UDP_IP, UDP_PORT))
    else:
        print("Invalid command. Use one from set: ", key_set)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()