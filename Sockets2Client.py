import socket

#IPn ja portin maaritys
SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall("This is from Client")

#Vastaanottaa dataa(viestin) clientilta, jonka tulostaa ulos serverilla. Antamalla clientille komennon "bye" sulkee clientin.
while True:

    in_data =  client.recv(1024)
    print("From Server: " + in_data)
  
    out_data = raw_input()
    client.sendall(out_data)
  
    if out_data=='bye':
        break
    
client.close()