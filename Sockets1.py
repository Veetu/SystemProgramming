import socket 
 
def find_service_name(): 
    protocolname = 'tcp' 
    for port in range (1, 100): 
        try:
            print ("There is %s service in port %s" %(socket.getservbyport(port, protocolname), port))

        except:
            print("There is no service in port %s" %(port))
     
if __name__ == '__main__': 
    find_service_name() 