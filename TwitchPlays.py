
import socket
import time
from pynput.keyboard import Key, Controller
import re
 
keyboard = Controller()

server = 'irc.chat.twitch.tv'
port = 6667
nickname = '------------'
token = 'oauth:----------------------'
channel = '-------------'
 
Listening = True
 
s = socket.socket()
s.connect((server, port))
s.send("PASS {}\r\n".format(token).encode("utf-8"))
s.send("NICK {}\r\n".format(nickname).encode("utf-8"))
s.send("JOIN #{}\r\n".format(channel).encode("utf-8"))


connected = False
run = True

def loop(Listening):
                while True:
                    if Listening == True:

#############################################################################################################################################
#######################################LEFT ANALOG STICK KEYS####################################################
#############################################################################################################################################
 
                        if message.strip().lower() == "up":
                            keyboard.press(Key.up)
                            time.sleep(0.15)
                            keyboard.release(Key.up)
                            print('Up Was Used')
                            break
                        if message.strip().lower() == "down":
                            keyboard.press(Key.down)
                            time.sleep(0.15)
                            keyboard.release(Key.down)
                            print('Down Was Used')
                            break
                        if message.strip().lower() == "left":
                            keyboard.press(Key.left)
                            time.sleep(0.15)
                            keyboard.release(Key.left)
                            print('Left Was Used')
                            break
                        if message.strip().lower() == "right":
                            keyboard.press(Key.right)
                            time.sleep(0.15)
                            keyboard.release(Key.right)
                            print('Right Was Used')
                            break

#############################################################################################################################################
######################################MAIN ACTION BUTTONS########################################################################
#############################################################################################################################################
                    
                        if message.strip().lower() == "a":
                            keyboard.press('a')
                            time.sleep(0.15)
                            keyboard.release('a')
                            print('A Was Used')
                            break
                        if message.strip().lower() == "b":
                            keyboard.press('b')
                            time.sleep(0.15)
                            keyboard.release('b')
                            print('B Was Used')
                            break
                        if message.strip().lower() == "x":
                            keyboard.press('x')
                            time.sleep(0.15)
                            keyboard.release('x')
                            print('X Was Used')
                            break
                        if message.strip().lower() == "y":
                            keyboard.press('y')
                            time.sleep(0.15)
                            keyboard.release('y')
                            print('Y Was Used')
                            break
                        
#############################################################################################################################################
##############################################LEFT|RIGHT TRIGGER AND BUMPERS######################################################################
#############################################################################################################################################
                    
                        if message.strip().lower() == "r":
                            keyboard.press('r')
                            time.sleep(0.15)
                            keyboard.release('r')
                            print('R Was Used')
                            break
                        if message.strip().lower() == "l":
                            keyboard.press('l')
                            time.sleep(0.15)
                            keyboard.release('l')
                            print('L Was Used')
                            break
                        if message.strip().lower() == "zr":
                            keyboard.press('t')
                            time.sleep(0.15)
                            keyboard.release('t')
                            print('ZR Was Used')
                            break
                        if message.strip().lower() == "zl":
                            keyboard.press('k')
                            time.sleep(0.15)
                            keyboard.release('k')
                            print('ZL Was Used')
                            break
                                                
#############################################################################################################################################
#########################################################RIGHT ANALOG STICK###################################################################
#############################################################################################################################################
                        
                        if message.strip().lower() == "rup":
                            keyboard.press('8')
                            time.sleep(0.15)
                            keyboard.release('8')
                            print('RUp Was Used')
                            break
                        if message.strip().lower() == "rright":
                            keyboard.press('6')
                            time.sleep(0.15)
                            keyboard.release('6')
                            print('R-Right Was Used')
                            break
                        if message.strip().lower() == "rdown":
                            keyboard.press('2')
                            time.sleep(0.15)
                            keyboard.release('2')
                            print('R-Down Was Used')
                            break
                        if message.strip().lower() == "rleft":
                            keyboard.press('4')
                            time.sleep(0.15)
                            keyboard.release('4')
                            print('R-Left Was Used')
                            break

#############################################################################################################################################
#############################################################DIRECTIONAL PAD#################################################################
#############################################################################################################################################
                        
                        if message.strip().lower() == "dup":
                            keyboard.press('8')
                            time.sleep(0.15)
                            keyboard.release('8')
                            print('D-Up Was Used')
                            break
                        if message.strip().lower() == "dright":
                            keyboard.press('6')
                            time.sleep(0.15)
                            keyboard.release('6')
                            print('D-Right Was Used')
                            break
                        if message.strip().lower() == "ddown":
                            keyboard.press('2')
                            time.sleep(0.15)
                            keyboard.release('2')
                            print('D-Down Was Used')
                            break
                        if message.strip().lower() == "dleft":
                            keyboard.press('4')
                            time.sleep(0.15)
                            keyboard.release('4')
                            print('D-Left Was Used')
                            break

#############################################################################################################################################
###########################################################PLUS AND MINUS################################################################
#############################################################################################################################################
                        
                        if message.strip().lower() == "plus":
                            keyboard.press('+')
                            time.sleep(0.15)
                            keyboard.release('+')
                            print('Plus Was Used')
                            break
                        if message.strip().lower() == "minus":
                            keyboard.press('-')
                            time.sleep(0.15)
                            keyboard.release('-')
                            print('Minus Was Used')
                            break
                    else:
                        print("Stopped Listening")
                        time.sleep(.25)
                        Listening= True
                        
                        #so we don't send messages too fast
        

while run:
    response = s.recv(2048).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        print('Pong')
    else:
        username = re.search(r"\w+", response)
        CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        
        message = CHAT_MSG.sub("", response).rstrip('\n')
 
        if 'End of /NAMES list' in message:
            connected = True
            print('Listening to ', channel)
 
        if connected == True:  
            if 'End of /NAMES list' in message:
                pass
            else:
                loop(Listening)