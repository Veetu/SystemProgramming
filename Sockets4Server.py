#Ennen tata tehtavaa paivitin pythonini 2.7.(?) versioon 3.9.4, koska aiemmissa tehtavissa ilmeni ongelmia turhan vanhaa pythonia kaytettaessa
from threading import Thread
import socket
 
 
#Luokka mainloop
class MainLoop:
    #tekee threadeista listan  
    def __init__(self):
        self.thread_list = []
 
    #mikäli "SUBSCRIBED" vastaanottaa teksinä aiheen ja viestin
    def send_to_conns(self, topic, msg):
        for conn in self.thread_list:
            conn.send_if_subscribed(topic, msg)
 
    #luo socketin, annettu IP osoite ja sen portti
    def run(self):
        s = socket.socket()          
        host = "127.0.0.1"           
        port = 50000                 

        #tulostaa seuraavat tiedot
        print("Server started!")
        print("Waiting for clients...")
 
        print(host, port)
        s.bind((host, port))
 
        #kuuntelee maarittamattoman maaran clientteja
        s.listen()
        while True:
            c, addr = s.accept()
            tcp_thread = TCPThread(self, c, addr)
            tcp_thread.start()
            self.thread_list.append(tcp_thread)
 
 
#Toinen luokka, jossa serveri, yhdeydet ja osoitteet. Tekee aiheista listan. Printtaa uuden yhteyden ja sen osoitteen 
class TCPThread(Thread):
    def __init__(self, server, conn, addr):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr
        self.server = server
        self.topics = []
        print(f"New connection: {self.addr}")
 
    def run(self):
        while True:
            msg = self.conn.recv(1024).decode()
            print(f"Message from {self.addr}: {msg}")
            #jos viesti muodossa: SUBSCRIBE/TOPIC, tallentaa ja printtaa tiedot
            if msg.startswith("SUBSCRIBE"):
                _, topic = msg.split("/")
                print(f"{self.addr} subscribed topic: {topic}")
                self.topics.append(topic)
            #mikäli taas viesti muodossa: PUBLISH/TOPIC/MESSAGE, "julkaisee" annettuun aiheeseen viestin
            elif msg.startswith("PUBLISH"):
                _, topic, msg = msg.split("/")
                print(f"{self.addr} published to topic {topic}: {msg}")
                self.server.send_to_conns(
                    topic=topic,
                    msg=f"{topic}/{msg}"
                )
 
    #lahettaa "tilaukselle" annetut tiedot
    def send_if_subscribed(self, topic, msg):
        if topic in self.topics:
            self.conn.sendall(msg.encode())
 
    #sulkee yhteyden
    def close(self):
        self.conn.close()
 
 
ml = MainLoop()
ml.run()