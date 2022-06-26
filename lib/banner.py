from colorama import Fore
from datetime import datetime
from time import sleep 
from os import system 
from lib.colors import c
                                
g = c.green
b = c.blue   

def terminal_logo(msg):
     result = input(c.red+" ┌─["+c.lcyan+"Web-Killer"+c.re+"/"+c.lgreen+msg+c.red+"""] 
 └──╼ """+c.re+"$ "+c.pink)
     return result


def terminal_Logo(msg):
     print(c.red+" ┌─["+c.lcyan+"Web-Killer"+c.re+"/"+c.lgreen+msg+c.red+"""] 
└──╼ """+c.re+"$ "+c.pink)   

def print_slow(banner):  
  for line in banner.split("\n"):
       sleep(0.1)
       print(line)


def logo():
        print(Fore.CYAN+"""
    _   _    _    ____  _   _ _____     ___  _____ ___  ____  
    | | | |  / \  / ___|| | | |_ _\ \   / / \|_   _/ _ \|  _ \ 
    | |_| | / _ \ \___ \| |_| || | \ \ / / _ \ | || | | | |_) |
    |  _  |/ ___ \ ___) |  _  || |  \ V / ___ \| || |_| |  _ < 
    |_| |_/_/   \_\____/|_| |_|___|  \_/_/   \_\_| \___/|_| \_\
""")   
 
               
def Show_menu():
        print(Fore.RESET+ f"\ndate : {datetime.now()}\r")
        sleep(0.1)
        print(Fore.RED+"[1]"+Fore.YELLOW+" Directory BruteForce")
        sleep(0.1)
        print(Fore.RED + "[2] " + Fore.YELLOW + "Check BTC wallet" )
        sleep(0.1)
        print(Fore.RED + "[3] " + Fore.YELLOW + "Network Tools" )
        sleep(0.1)  
        print(Fore.RED + "[4] " + Fore.YELLOW + "Hash " +c.pink+"[coming soon ]")
        sleep(0.1)  
        print(Fore.RED + "[9] " + Fore.YELLOW + "Developer")
        sleep(0.1)
        print(Fore.RED + "[10] " + Fore.YELLOW + "Exit")
        
                


def netwok_banneMr():
    banner =(f"""\n{g}[1]{b} - 𝚈𝚘𝚞𝚛 𝙸𝙿 𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗

{g}[2]{b} - 𝚂𝚑𝚘𝚠 𝙷𝚃𝙿𝙿 𝙷𝙴𝙰𝙳𝙴𝚁 

{g}[3]{b} - 𝙵𝚒𝚗𝚍 𝚂𝚑𝚊𝚛𝚎𝚍 𝙳𝙽𝚂

{g}[4]{b} - 𝙳𝙽𝚂 𝙻𝚘𝚘𝚔𝚄𝚙

{g}[5]{b} - Back MainMenu
""")
    print_slow(banner=banner)



def directory_banner():
    banner =(f"""{g}[1]{b} - Check all 17900 directories

{g}[2]{b} - php 

{g}[3]{b} - Admin Finder

{g}[4]{b} - wordpress press

{g}[5]{b} - Back MainMenu

""")
    print_slow(banner=banner)



def network_banner(method_name):
   if method_name == "shareDns":
      banner = (c.cyan+"""
_____ _                     ______
/  ___| |                    |  _  \
\ `--.| |__   __ _ _ __ ___  | | | |_ __  ___
 `--. \ '_ \ / _` | '__/ _ \ | | | | '_ \/ __|
/\__/ / | | | (_| | | |  __/ | |/ /| | | \__ \
\____/|_| |_|\__,_|_|  \___| |___/ |_| |_|___/
      """+c.re)
   elif method_name == "ip":
        banner = (c.cyan+"""
___________   _____ _   _ ______ _____
|_   _| ___ \ |_   _| \ | ||  ___|  _  |
  | | | |_/ /   | | |  \| || |_  | | | |
  | | |  __/    | | | . ` ||  _| | | | |
 _| |_| |      _| |_| |\  || |   \ \_/ /
 \___/\_|      \___/\_| \_/\_|    \___/
        """)
   elif method_name == "http":
        banner = (c.cyan+"""
_           _  _  _  _  _  _           _  _  _  _  _  _  _  _  _
(_)         (_)(_)(_)(_)(_)(_)         (_)(_)(_)(_)(_)(_)(_)(_)(_)_
(_)         (_)      (_)                     (_)      (_)        (_)
(_) _  _  _ (_)      (_)                     (_)      (_) _  _  _(_)
(_)(_)(_)(_)(_)      (_)                     (_)      (_)(_)(_)(_)
(_)         (_)      (_)                     (_)      (_)
(_)         (_)      (_)                     (_)      (_)
(_)         (_)      (_)                     (_)      (_)
         """)
   elif method_name == "DnsLookUp":
        banner = (c.cyan+"""
    ______             _                 _      _   _______
|  _  \           | |               | |    | | | | ___ \
| | | |_ __  ___  | |     ___   ___ | | __ | | | | |_/ /
| | | | '_ \/ __| | |    / _ \ / _ \| |/ / | | | |  __/
| |/ /| | | \__ \ | |___| (_) | (_) |   <  | |_| | |
|___/ |_| |_|___/ \_____/\___/ \___/|_|\_\  \___/\_|
        """)  
   elif method_name == "main":
       banner = (c.cyan+"""
_   _      _                      _
| \ | |    | |                    | |
|  \| | ___| |___      _____  _ __| | __
| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |\  |  __/ |_ \ V  V / (_) | |  |   <
\_| \_/\___|\__| \_/\_/ \___/|_|  |_|\_\
       """+c.re)
   print_slow(banner=banner)
   
   
   
def Dir_Option_banner(method_name):
   if method_name == "main":
     banner = (c.cyan+"""
+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+
|D|i|r|e|c|t|o|r|y| |B|r|u|t|e| |F|o|r|c|e|
+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+
     """)
   elif method_name == "All":
     banner = (c.cyan+"""
_        _  _     _  _     _  _  _  _        _
     _(_)_     (_)(_)   (_)(_)   (_)(_)(_)(_)      (_)
   _(_) (_)_      (_)      (_)    (_)      (_)_  _  _   _       _  _
 _(_)     (_)_    (_)      (_)    (_)        (_)(_)(_) (_)_  _ (_)(_)
(_) _  _  _ (_)   (_)      (_)    (_)        (_)   (_)   (_)(_)
(_)(_)(_)(_)(_)   (_)      (_)    (_)       _(_)   (_)   (_)
(_)         (_) _ (_) _  _ (_) _  (_)_  _  (_)   _ (_) _ (_)
(_)         (_)(_)(_)(_)(_)(_)(_)(_)(_)(_)(_)   (_)(_)(_)(_)

     """)
   elif method_name == "php":
     banner = (c.cyan+"""
_  _  _  _             _           _           _  _  _  _
(_)(_)(_)(_)_          (_)         (_)         (_)(_)(_)(_)_
(_)        (_)         (_)         (_)         (_)        (_)
(_) _  _  _(_)         (_) _  _  _ (_)         (_) _  _  _(_)
(_)(_)(_)(_)           (_)(_)(_)(_)(_)         (_)(_)(_)(_)
(_)                    (_)         (_)         (_)
(_)                    (_)         (_)         (_)
(_)                    (_)         (_)         (_)
     """)
   elif method_name == "admin":
     banner = (c.cyan+"""
_                   _                    _
     _(_)_                (_)                  (_)
   _(_) (_)_      _  _  _ (_)  _  _   _  _   _  _     _  _  _  _
 _(_)     (_)_  _(_)(_)(_)(_) (_)(_)_(_)(_) (_)(_)   (_)(_)(_)(_)_
(_) _  _  _ (_)(_)        (_)(_)   (_)   (_)   (_)   (_)        (_)
(_)(_)(_)(_)(_)(_)        (_)(_)   (_)   (_)   (_)   (_)        (_)
(_)         (_)(_)_  _  _ (_)(_)   (_)   (_) _ (_) _ (_)        (_)
(_)         (_)  (_)(_)(_)(_)(_)   (_)   (_)(_)(_)(_)(_)        (_)
     """)
   elif method_name == "wordpress":
     banner = (c.cyan+"""
_    _               _  ______
| |  | |             | | | ___ \
| |  | | ___  _ __ __| | | |_/ / __ ___  ___ ___
| |/\| |/ _ \| '__/ _` | |  __/ '__/ _ \/ __/ __|
\  /\  / (_) | | | (_| | | |  | | |  __/\__ \__ \
 \/  \/ \___/|_|  \__,_| \_|  |_|  \___||___/___/
     """)
   print_slow(banner=banner)
   
   
   
   
def bitcoin_check_banner():
  banner =(c.cyan+"""
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
|B|i|t|c|o|i|n| |w|a|l|l|e|t| |c|h|e|c|k|e|r|
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+
  """)
  print_slow(banner=banner) 
