import socket
import Tkinter as tk

UDP_IP = "192.168.1.5"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    key_set = ['w', 's', 'a', 'd', 'q', 'e']

    if key_press.lower() in key_set:
        sock.sendto(key_press.lower(), (UDP_IP, UDP_PORT))
    else:
        print("Hell no to the no no ...")

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()