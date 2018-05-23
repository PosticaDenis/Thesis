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
                car.forward(TF, 40, 40, 40, 40)
            elif option == 's':
                car.reverse(TF, 75, 75, 75, 75)
            elif option == 'a':
                car.fullleft(TF, 60, 60, 80, 80)
            elif option == 'd':
                car.fullright(TF, 80, 80, 60, 60)
            elif option == 'q':
                car.forward(TF, 0, 0, 80, 80)
            elif option == 'e':
                car.forward(TF, 80, 80, 0, 0)
            elif option == 'z':
                car.reverse(TF, 0, 0, 80, 80)
            elif option == 'x':
                car.reverse(TF, 80, 80, 0, 0)
            else:
                car.stop()
        else:
            car.stop()
        
except KeyboardInterrupt:
    sock.close()
    