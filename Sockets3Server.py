import socket, threading

class ClientThread(threading.Thread):

#luodaan uusi socketti ja lista yhdistäville clienteille. Printtaa uuden yhteyden, kuten edellinenkin serveri. (clientAddress = clientin osoite, clientsocket = uusi socketti yhdistetyille clienteille, list = lista, johon tallennetaan yhdistetyt clientit)
    def __init__(self,clientAddress,clientsocket, list):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
        self.list = list

#msg tallentaa annetun viestin, jonka printtaa "from client:" peraan. "dataksi" vaaditaan kayttajalta jokin inputti = teksti.
    def run(self):
        print ("Connection from : ", clientAddress)

        msg = ''
        data = True

        while True:
            data = self.csocket.recv(2048)
            msg = data
            if msg=='bye':
              break
            print ("from client: " + msg)

#for looppi, joka vastaanottaa viestin clientilta ja lahettaa sen muille clienteille. Mikali viesti on yllamainittu "bye" clientti katkaisee yhteyden serveriin, jonka serveri printtaa.
            for i in range(len(self.list)):
                print("sending to: ", i)
                self.list[i].sendall(msg)
        print ("Client at ", clientAddress , " disconnected...")

#IPn ja portin maaritys
LOCALHOST = "127.0.0.1"
PORT = 8080

#Maaritetaa server. Serverin kaynnistyessa printtaa siitä ilmoituksen "Server started" ja "Waiting for client request"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")

#Lista johon tallennetaan uudet threadit, jotka pitavat sisallaan tiedot clientin osoitteesta jne.
threadList = []

#While looppi, joka on asetettu tässä tapauksessa kuuntelemaan kolmea clienttia.  Printtaa yhdistettyjen clientien lukumaaran.
while True:
    server.listen(3)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock, threadList)
    threadList.append(clientsock)
    print(threadList.count)
    newthread.start()

#Tassa tehtavassa oli pienia vaikeuksia, silla clientti1 ei syysta tai toisesta onnistu vastaanottamaan clientin2 viestia serverilta ennen, kuin client1 on lahettanyt oman viestinsa. 