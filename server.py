import socket
import sys
from time import sleep

HOST = 'localhost'
PORT = 8080


# 1 create du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 connect socket to address and port :

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    # 3 waiting for client connexion:

    print("Server ready and awaiting request ...")
    # our server can connect only one client (mySocket.listen(1))
    mySocket.listen(1)

    # 4 establish connexion with client :
    connexion, address = mySocket.accept()

    print("Client connected, IP address %s, port %s" % (address[0], address[1]))

    # server send welcome message :
    msgServer = "You are connected you can start dialog."
    connexion.send(msgServer.encode("Utf8"))
    i = 0
    while True:
        #it is here that you can add the code witch print data from myo
        sleep(1)
        i = i+1
        msgServer = str(i)
        connexion.send(msgServer.encode("Utf8"))

    connexion.close()
