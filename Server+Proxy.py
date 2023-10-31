# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:21:39 2023

@author: Maya
"""
import socket
from datetime import datetime

#time functions
Date= datetime.now()
Time= Date.strftime("%H:%M:%S")

#Socket intialization
ServerSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#gethostbyname :IP address of the local host
#gethostname:returns the host name of the current system under
#which the Python interpreter is executed.
Name= socket.gethostbyname(socket.gethostname())
Port= 3566
#Binding
ServerSocket.bind((Name,Port))
#Listen 
ServerSocket.listen()

#Intializing Proxy Server (Acts as a client wrt the web page)
Proxy=socket.socket(socket.AF_INET, socket.SOCK_STREAM )
print("Waiting for Connection...")

while True: #So that the server can take multiple requests
    ClientSocket,address= ServerSocket.accept()
    print("Connected Successfully!")
    
    RecieveRequest=ClientSocket.recv(4096).decode()
    #Accessing the IP address(Remove the get statement and its complements)
    ActualIP=RecieveRequest.split()
    #Message with exact time of the actual request
    print("Request: "+ RecieveRequest)
    print("Time of request :"+ Time)
    
   
    try:
        Proxy.connect((ActualIP[4],80)) #IP of webpage+ port of web
    except:
        print("ERROR! Unreachable IP address") #display error to the client
        #return error to client
        ProxyResponse= "ERROR! Unreachable IP address"
        break
    #send the Request to the webpage
    Proxy.send(RecieveRequest.encode())        
    print("Request is Sent from proxy to web at: "+Time)
    #Recieve the Response from the webpage
    ProxyResponse= Proxy.recv(4096).decode()
    print("Response Recieved from web to proxy at: "+Time)
    
    Proxy.close()
     
    break #for the sake of this Assignment we wont take more that one connection so we break
#send the Response to the client
ClientSocket.send(ProxyResponse.encode())
print("Response sent to client at: "+ Time)
ServerSocket.close()
