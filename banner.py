from colorama import Fore
from datetime import datetime
from time import sleep 
from os import system 
def Show_menu():
        print(Fore.CYAN+"""_   _    _    ____  _   _ _____     ___  _____ ___  ____  
| | | |  / \  / ___|| | | |_ _\ \   / / \|_   _/ _ \|  _ \ 
| |_| | / _ \ \___ \| |_| || | \ \ / / _ \ | || | | | |_) |
|  _  |/ ___ \ ___) |  _  || |  \ V / ___ \| || |_| |  _ < 
|_| |_/_/   \_\____/|_| |_|___|  \_/_/   \_\_| \___/|_| \_\
""")   
        print(Fore.RESET+ f"\ndate : {datetime.now()}\r")
        sleep(0.1)
        print(Fore.RED+"[1]"+Fore.YELLOW+" Check site directory ")
        sleep(0.1)
        print(Fore.RED + "[2] " + Fore.YELLOW + "Check BTC wallet" + Fore.GREEN + "[ Use vpn ]")
        sleep(0.1)
        print(Fore.RESET + Fore.RED +"[3] " + Fore.YELLOW + "Password Generator")
        sleep(0.1)
        print(Fore.RED + "[4] " + Fore.YELLOW + "Show your Area Number ")
        sleep(0.1)
        print(Fore.RED + "[5] " + Fore.YELLOW + "Calculate number")
        print("")
        sleep(0.1)
        
        
        
def Back_menu():
    sleep(1)
    data = input(Fore.GREEN+"\n[+] Do You Want To Back menu ?")
    if data.lower() == "y":
        pass
    else:
      exit(Fore.CYAN+"GoodBye")
