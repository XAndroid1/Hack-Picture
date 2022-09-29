import os.path
from os import *
import sys
import time
R='\033[1;31m'#احمر 
R='\033[1;31m'
G='\033[1;32m'#اخضر 
Y='\033[1;33m'
C='\033[1;36m'
X = '\033[1;33m' #اصفر
W='\033[1;37m'#ابيض 
A='\033[1;35m'
xan = ('''\033[1;33m___________________________________________________\033[;32m

 X\033[1;31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[1;32m
 XXXX\033[1;31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXX\033[1;31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXXXXXX\033[1;31mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXXXXXXXXX\033[1;37mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXXXXXXXXXXXX\033[1;37mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXXXXXXXXX\033[1;37mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXXXXXX\033[1;30mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXXXXX\033[1;30mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m XXXX\033[1;30mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
\033[1;32m X\033[1;30mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX		
\033[1;31m___________________________________________________

 \033[1;30m<< \033[1;36mS\033[1;37mU\033[1;33mD\033[1;35mA\033[1;31mN\033[1;30m >>                          \033[1;30m<< \033[1;32mX-\033[1;36mA\033[1;33mN\033[1;31mD\033[1;35mR\033[1;36mO\033[1;33mI\033[1;31mD \033[1;30m>>
 \033[1;31m_______________________________________________________
 
\033[1;35m Telegram:>\033[1;32mhttps://t.me/X1Android
 \033[1;35mFacebook:>\033[1;32mhttps://www.facebook.com/X.11Android
________________________________________________________

 ''')
os.system("clear")
system('sleep 0.6')
for e in xan:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(5/400)
system('sleep 0.2')
a = input (C +"  •~ " + R +"Enter bassword : >> "+ G)
if a == 'XAndroid':
	print ('bassword...')
	system('sleep 2.2')
	print ('plese ...')
	system('sleep 2	.2')
	os.system('clear')
	os.system('python .App.py')
else:
	e = ('''\033[1;31m______
| ____|_ __ _ __ ___  _ __
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |
|_____|_|  |_|  \___/|_|
''')
	print (e)
	print (R+60*' Error ')
	sys.exit()