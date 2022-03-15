from socket import *
from colorama import Fore, Back, Style
import platform
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
def main():
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', portset))
    serverSock.listen(1)
    connectionSock, addr = serverSock.accept()

    print(str(addr), '\nConnected.')
    recvData = connectionSock.recv(1024)
    print(recvData.decode('utf-8'))
    recvData = connectionSock.recv(1024)
    print(recvData.decode('utf-8'))
    while True:
        sendData = input('Command:')
        if sendData == "Exit_Command":
            quit()
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
