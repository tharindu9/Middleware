# server.py 
import socket                                         
import time

#function for the  substraction
def substraction(num1, num2):
    if num1 > num2:
        return num1-num2
    else:
        return num2-num1

#function for the addition of two numbers
def addition(num1,num2):
    return num1+num2


def multipication(num1,num2):
    return num1*num2

def modul(num1,num2):
    return num1%num2

def getparams(data):
    param_string = data.split("\n")[2]
    params = param_string.split("&")
    
    arr = []
    for param in params:
        arr.append(param.split("=")[1])
    if (len(arr) != 2):
        arr[1],arr[2]=int(arr[1]),int(arr[2])
        print arr
    return arr
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost" #socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      
    
    print("Got a connection from %s" % str(addr))
    data = clientsocket.recv(1024)
    
    print(data) #.split("\n"))
    params = getparams(data)

    if (len(params)<2):
        resp = "Parameter length doesn't match"
    else:
        method = params[0]
        if(method=='add'):
            resp = str(addition(params[1],params[2]))

        if(method=='sub'):
            resp = str(substraction(params[1],params[2]))
        if(method=='mul'):
            resp = str(multipication(params[1],params[2]))
        if(method=='mod'):
            resp = str(modul(params[1],params[2]))

        
        
    clientsocket.send(resp)
    clientsocket.close()
