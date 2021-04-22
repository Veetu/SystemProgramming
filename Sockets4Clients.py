#Ennen tata tehtavaa paivitin pythonini 2.7.(?) versioon 3.9.4, koska aiemmissa tehtavissa ilmeni ongelmia turhan vanhaa pythonia kaytettaessa
import socket
from threading import Thread
 
#IPn ja portin maariys 
SERVER = "127.0.0.1"
PORT = 50000
 

#Vastaanottavan threadin luokka 
class ReceiverThread(Thread):
    def __init__(self, client):
        super().__init__(daemon=True)
        self.client = client
 
    def run(self):
        while True:
            # format: TOPIC/MESSAGE, mihin topiciin halutaan kirjoittaa ja mita
            msg_contents = self.client.recv(1024).decode().split("/")
            print(f"New message to topic {msg_contents[0]}: {msg_contents[1]}")
 
 
client = socket.socket() 
client.connect((SERVER, PORT))
 
#kaynnistaa threadin
recv_thread = ReceiverThread(client)
recv_thread.start()

#pyytaa clientilta dataa(viestin, jossa "TOPIC" ja "MESSAGE" voivat olla vapaavalintaisia) muodossa PUBLISH/TOPIC/MESSAGE tai SUBSCRIBE/TOPIC. Mikali datana on teksti "bye" client katkaisee yhteyden serveriin.
while True:
    msg_contents = input("PUBLISH/TOPIC/MESSAGE or SUBSCRIBE/TOPIC, bye to exit> ")
    if msg_contents == 'bye':
        break
    if not (
        msg_contents.startswith("PUBLISH") or
        msg_contents.startswith("SUBSCRIBE")
            ):
        print("Use PUBLISH or SUBSCRIBE")
    print(msg_contents)
    client.send(msg_contents.encode())
 
#clientin sulku 
client.close()