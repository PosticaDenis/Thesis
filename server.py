import socket
import car_controller as car

TF = 0.065
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print('Received: ' + data)
        if data.lower() == 'w':
            car.forward(TF, 100, 100, 100, 100)
        elif data.lower() == 's':
            car.reverse(TF, 100, 100, 100, 100)
        elif data.lower() == 'a':
            car.fullleft(TF, 100, 100, 100, 100)
        elif data.lower() == 'd':
            car.fullright(TF, 100, 100, 100, 100)
        elif data.lower() == 'q':
            car.forward(TF, 25, 25, 100, 100)
        elif data.lower() == 'e':
            car.forward(TF, 100, 100, 25, 25)
        else:
            print("Hell no to the no no ...")
except KeyboardInterrupt:
    sock.close()
