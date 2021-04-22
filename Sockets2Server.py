import socket, threading

class ClientThread(threading.Thread):

#Ilmoittaa yhdistaneen clientin osoitteen. (clientAddress = yhdistävän clientin osoite, clientsocket = yhdistetylle clientille luotu socketti)
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

#msg tallentaa annetun viestin, jonka printtaa "from client:" peraan. Ikuisuuslooppi, joka paattyy vain jos veistina on "bye", silloin clientti katkaisee yhteyden serveriin ja serveri ilmoittaa siita.
    def run(self):
        print ("Connection from : ", clientAddress)

        msg = ''
        data = True

        while data:
            data = self.csocket.recv(2048)
            msg = data
            if msg=='bye':
              break
            print ("from client: " + msg)

            self.csocket.send(msg)
        print ("Client at ", clientAddress , " disconnected...")

#IPn ja portin maaritys
LOCALHOST = "127.0.0.1"
PORT = 8080

#Serverin maarittely
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")

#Asettaa serverin kuuntelemaan
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()