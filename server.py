import socket
import car_controller as car

TF = 0.035
UDP_IP = "192.168.1.5"
UDP_PORT = 5055

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

optionsDic = {    'w' : car.forward(TF, 100, 100, 100, 100),
               's' : car.reverse(TF, 100, 100, 100, 100),
               'a' : car.fullleft(TF, 100, 100, 100, 100),
               'd' : car.fullright(TF, 100, 100, 100, 100),
               'q' : car.forward(TF, 25, 25, 100, 100),
               'e' : car.forward(TF, 100, 100, 25, 25),
}
options = ['w', 's', 'a', 'd', 'q', 'e', 'z', 'x']

try:
    while True:
        option, address = sock.recvfrom(256)
        option = option.decode()
        
        if option in options:
            print("Received command: ", option)
            
            if option == 'w':
                car.forward(TF, 100, 100, 100, 100)
            elif option == 's':
                car.reverse(TF, 100, 100, 100, 100)
            elif option == 'a':
                car.fullleft(TF, 85, 85, 100, 100)
            elif option == 'd':
                car.fullright(TF, 100, 100, 85, 85)
            elif option == 'q':
                car.forward(TF, 0, 0, 100, 100)
            elif option == 'e':
                car.forward(TF, 100, 100, 0, 0)
            elif option == 'z':
                car.reverse(TF, 0, 0, 100, 100)
            elif option == 'x':
                car.reverse(TF, 100, 100, 0, 0)
            else:
                car.stop()
        else:
            car.stop()
        
except KeyboardInterrupt:
    sock.close()
    