#******T.me/PYTHONTE******** 
#Owner T.me/LooQaat-
#AUTHR T.me/HASHIVATOR
#Bug fixes and complements
#‐-----------------T.me/HASHIVATOR
from requests import get
from ipapi import location
from random import sample
from colorama import Fore
from phonenumbers import geocoder, parse
from datetime import datetime
from itertools import count
from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
from os import system
all = l + u + d + p
#installing
print(Fore.RED+"INSTSLLING  DOCUMENT\n\n\n\n\n\n\n ")
system(Fore.CYAN+"pip install requests")  
system("pip install phonenumbers")  
system("pip install ipapi")  
system("pip install colorama") 
system("pip install itertools")  
system("pip install datetime")
system("clear")

class Style:
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'
    CYAN = '\033[96m'

ok = True
while True:

    
    try:
        print(Style.CYAN+"""_   _    _    ____  _   _ _____     ___  _____ ___  ____  
| | | |  / \  / ___|| | | |_ _\ \   / / \|_   _/ _ \|  _ \ 
| |_| | / _ \ \___ \| |_| || | \ \ / / _ \ | || | | | |_) |
|  _  |/ ___ \ ___) |  _  || |  \ V / ___ \| || |_| |  _ < 
|_| |_/_/   \_\____/|_| |_|___|  \_/_/   \_\_| \___/|_| \_\
""")    
        print(Fore.RESET+Style.BOLD + f"\ndate : {datetime.now()}\r")
        print(Fore.RED+"[1]"+Fore.YELLOW+" Check site directory ")
        print(Fore.RED + "[2] " + Fore.YELLOW + "Show your ip " + Fore.GREEN + "[ Use vpn ]")
        print(Fore.RESET + Fore.RED +"[3] " + Fore.YELLOW + "Password Generator")
        print(Fore.RED + "[4] " + Fore.YELLOW + "Show your Area Number ")
        print(Fore.RED + "[5] " + Fore.YELLOW + "Calculate number")
        print(Fore.RED + "[6] " + Fore.YELLOW + "Fun")  
        print("")
        a = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX)
        print(Fore.RESET)
        if a == "1":
          try:
           print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
           inp = "https://"+input(Fore.GREEN+"Enter the URL"+Fore.LIGHTRED_EX+" [with out https://] :\n")+'/'
           with open('directories.txt','r') as foo:
                for i in foo:
                   h = get(inp+i)
                   if h.status_code == 200:
                       print(Fore.GREEN+"[+]"+inp+i)
                   else:
                       print (Fore.RED+"[!] "+inp+i)
          except KeyboardInterrupt:
                 exit(Fore.CYAN+"\nGoodBye")
        elif a == "2":
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            ip = get("https://api.ipify.org").text
            print('\n' + Fore.MAGENTA + ip + Fore.RESET)
            http = get("https://api.ipify.org").text
            cou = location(http)["country"]
            if cou == "IR":
                print(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + Style.BOLD + "BLOCKED" + Style.END + " from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " + Style.UNDERLINE + Fore.GREEN + cou +"\n\n\n\n"+ Style.END + Fore.RESET)
                
        elif a == "3":
            try:
                print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
                length = int(input("Enter length of password: "))
            except ValueError:
                print("Length can't be string or float or empty ...")
                pass
            
            if length < 8 or length > 100:
                print("Password length must be between 8 and 100!")
                ok = False
                # and try again
            elif ok == True:
                password = "".join(sample(all,length))
                print(Fore.GREEN + "Your pass is: " + Fore.YELLOW + "|--> "+ Style.UNDERLINE + password + Style.END + " <--|" + Fore.GREEN)
            pass
        elif a == "4":
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            numbers = input(Fore.LIGHTGREEN_EX+"Enter Number\t \nWith code area(+98):\n")
            print(Fore.LIGHTYELLOW_EX+"this number countary name is ")
            ph_number = parse(numbers)
            print(geocoder.description_for_number(ph_number,"fa"))
            print("\n\n\n")
        elif a == "5":
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            num_1 = int(input("Send first number to calc: "))
            num_2 = int(input("Send second number to calc: "))
            action = input(Fore.CYAN+"Which one: * + / - : ")
            if action == "+":
                print(Fore.LIGHTYELLOW_EX+"Your answers : ")
                print(num_1 + num_2)
                print("\n\n")
            elif action == "-":
                print(Fore.YELLOW+"Your answers : ")
                print(+num_1 - num_2)
                print("\n\n")
            elif action == "*":
                print(Fore.YELLOW+"Your answers : ")
                print(num_1 * num_2)
                print("\n\n")
            elif action == "/":
                print(Fore.YELLOW+"Your answers : \n")
                print(num_1 / num_2)
                print("\n\n")
    except KeyboardInterrupt:
        print("",flush=True)
        print("GoodBye!",flush=True)
        exit(1)
    else:
        try:
            if a == "6":
                print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
                for i in count(2,2):
                    if i == 198618:
                        print(Style.CYAN+"\nscrapping your file")
                        break
                    else:
                        print(i)
        except(RuntimeError,KeyboardInterrupt):
            print(" ", end="", flush=True)
            
            continue
