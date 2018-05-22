import socket
import car_controller as car

TF = 0.065
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

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
        options[option]
        
except KeyboardInterrupt:
    sock.close()