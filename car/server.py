import socket
import car_controller as car

TF = 0.035
UDP_IP = "192.168.1.5"
UDP_PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

options = ['w', 's', 'a', 'd', 'q', 'e', 'z', 'x']

try:
    while True:
        option, address = sock.recvfrom(256)
        option = option.decode()
        
        if option in options:
            print("Received command: ", option)
            
            if option == 'w':
                car.forward(TF, 30, 30, 30, 30)
            elif option == 's':
                car.reverse(TF, 30, 30, 30, 30)
            elif option == 'a':
                car.fullleft(TF, 30, 30, 50, 50)
            elif option == 'd':
                car.fullright(TF, 30, 30, 50, 50)
            elif option == 'q':
                car.forward(TF, 0, 0, 50, 50)
            elif option == 'e':
                car.forward(TF, 50, 50, 0, 0)
            elif option == 'z':
                car.reverse(TF, 0, 0, 50, 50)
            elif option == 'x':
                car.reverse(TF, 50, 50, 0, 0)
            else:
                car.stop()
        else:
            car.stop()
        
except KeyboardInterrupt:
    sock.close()
    