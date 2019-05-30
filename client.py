import socket, sys

HOST = 'localhost'
PORT = 8080

# 1) create socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) send connexion request to server:
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("connexion failed")
    sys.exit()

# 3)communicate with server :

msgServer = mySocket.recv(1024).decode("Utf8")
print("S>", msgServer)

while 1:
    #msgClient = input("C> ")
    #mySocket.send(msgClient.encode("Utf8"))
    msgServer = mySocket.recv(1024).decode("Utf8")
    print("S>", msgServer)
    #mySocket.send("new".encode("Utf8"))

# 4) close connexion :
print("Connexion ended.")
mySocket.close()