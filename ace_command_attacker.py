from socket import *
from colorama import Fore, Back, Style
import platform
import pyautogui
from io import StringIO
from time import sleep
import mouse
def return_print(*message):
	io=StringIO()
	print(*message,file=io,end="")
	return io.getvalue()
infor=platform.platform()
def choose():
    print("Choose an option:")
    print(Fore.BLUE+"[1] Port settings")
    print(Fore.RED+"[2] run acecommand")
    select=int(input())

    if select == 1:
        global portset
        portset=int(input("Port : "))
        print("Ports configured: %d"%portset)
        choose()
    elif select == 2:
        main()
def remotecontrol():
    sleep(1)
    while True:
                        if mouse.is_pressed("left"):
                                sendData="click:left"
                                connectionSock.send(sendData.encode('utf-8'))
                                sleep(0.5)
                        elif  mouse.is_pressed("right"):
                                sendData="click:right"
                                connectionSock.send(sendData.encode('utf-8'))
                                sleep(0.5)
                        else:
                            value=return_print(pyautogui.position())
                            value=value.split("(")
                            value=value[1].split(")")
                            value=value[0]#x=300,y=300
                            xpandyp=value.split(",")
                            xp=xpandyp[0].split("=")
                            xp=xp[1]
                            yp=xpandyp[1].split("=")
                            yp=yp[1]
                            pos=xp+","+yp

                            sendData=pos
                            connectionSock.send(sendData.encode('utf-8'))#300,300
                            sleep(0.1)
def main():
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', portset))
    serverSock.listen(1)
    global connectionSock,addr
    connectionSock, addr = serverSock.accept()

    print(str(addr), '\nConnected.')
    recvData = connectionSock.recv(1024)
    print(recvData.decode('utf-8'))
    while True:
        sendData = input('Command:')
        if sendData == "Exit_Command":
            quit()
        elif sendData == "Remote_Control":
            connectionSock.send(sendData.encode('utf-8'))
            remotecontrol()

        else:
            connectionSock.send(sendData.encode('utf-8'))
            recvData = connectionSock.recv(1024)
            print(recvData.decode('utf-8'))

print(Fore.GREEN+'''
                                                                                                                        ,,
      db                              .g8"""bgd                                                                         `7MM
     ;MM:                           .dP'     `M                                                                           MM
    ,V^MM.     ,p6"bo   .gP"Ya      dM'       `  ,pW"Wq.  `7MMpMMMb.pMMMb.  `7MMpMMMb.pMMMb.   ,6"Yb.  `7MMpMMMb.    ,M""bMM
   ,M  `MM    6M'  OO  ,M'   Yb     MM          6W'   `Wb   MM    MM    MM    MM    MM    MM  8)   MM    MM    MM  ,AP    MM
   AbmmmqMA   8M       8M""""""     MM.         8M     M8   MM    MM    MM    MM    MM    MM   ,pm9MM    MM    MM  8MI    MM
  A'     VML  YM.    , YM.    ,     `Mb.     ,' YA.   ,A9   MM    MM    MM    MM    MM    MM  8M   MM    MM    MM  `Mb    MM
.AMA.   .AMMA. YMbmd'   `Mbmmd'       `"bmmmd'   `Ybmd9'  .JMML  JMML  JMML..JMML  JMML  JMML.`Moo9^Yo..JMML  JMML. `Wbmd"MML.
''')
choose()
