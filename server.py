import socket
import car_controller as car

TF = 0.065
UDP_IP = "192.168.1.5"
UDP_PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

options = {    "w" : car.forward(TF, 100, 100, 100, 100),
               "s" : car.reverse(TF, 100, 100, 100, 100),
               "a" : car.fullleft(TF, 100, 100, 100, 100),
               "d" : car.fullright(TF, 100, 100, 100, 100),
               "q" : car.forward(TF, 25, 25, 100, 100),
               "e" : car.forward(TF, 100, 100, 25, 25),
}

try:
    while True:
        option, address = sock.recvfrom(256)
        print("Received command: ", option.decode())
        options[option.decode()]
        
except KeyboardInterrupt:
    sock.close()