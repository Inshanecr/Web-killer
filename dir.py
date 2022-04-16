#******T.me/PYTHONTE******** 
#Owner T.me/LooQaat-
#AUTHR T.me/HASHIVATOR
#Bug fixes and complements
#‐-----------------T.me/HASHIVATOR


#installing
from os import system
print("INSTSLLING  DOCUMENT\n\n\n\n\n\n\n ")
system("pip install requests")  
system("pip install phonenumbers")  
system("pip install ipapi")  
system("pip install colorama") 
system("pip install itertools")  
system("pip install datetime")
system("clear")
#libary


from requests import get
from ipapi import location
from random import sample
from colorama import Fore
from phonenumbers import geocoder, parse
from datetime import datetime
from itertools import count
from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
from directories import directorylist
all = l + u + d + p

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
""")      #HELP MENU
        print(Fore.RESET+Style.BOLD + f"\ndate : {datetime.now()}\r")
        print(Fore.RED+"[1]"+Fore.YELLOW+" Check site directory ")
        print(Fore.RED + "[2] " + Fore.YELLOW + "Check BTC wallet" + Fore.GREEN + "[ Use vpn ]")
        print(Fore.RESET + Fore.RED +"[3] " + Fore.YELLOW + "Password Generator")
        print(Fore.RED + "[4] " + Fore.YELLOW + "Show your Area Number ")
        print(Fore.RED + "[5] " + Fore.YELLOW + "Calculate number")
        print(Fore.RED + "[6] " + Fore.YELLOW + "Fun")  
        print("")
        a = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX)
        print(Fore.RESET)
        if a == "1": ##DIRECTORY
          try:
           print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
           inp = "https://"+input(Fore.GREEN+"Enter the URL"+Fore.LIGHTRED_EX+" [with out https://] :\n")+'/'
           data = directorylist
           for i in data: 
              h = get(inp+i)
              if h.status_code == 200:
                 print(Fore.GREEN+"[ + ]"+inp+i)
              else:
                 print (Fore.RED+"[!] "+inp+i)

          except KeyboardInterrupt:
                 exit(Fore.CYAN+"\nGoodBye")
        elif a == "2":##BITCOIN CHECK
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            ip = get("https://api.ipify.org").text
            print('\n' + Fore.MAGENTA + ip + Fore.RESET)
            http = get("https://api.ipify.org").text
            cou = location(http)["country"]
            if cou == "IR":
                exit(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + Style.BOLD + "BLOCKED" + Style.END + " from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " + Style.UNDERLINE + Fore.GREEN + cou +"\n\n\n\n"+ Style.END + Fore.RESET)
            else:
                 try:
                  wallet = input(Fore.CYAN+"\nSend your bitcoin wallet address please: \n")
                  wallet_ceck = get("https://blockchain.com/btc/address"+wallet)
                  if wallet_ceck.status_code == 200:
                    print(f"Your wallet address is correct :\n {Wallet}")
                  else:
                    print(Fore.RED+"wrong Wallet") 
                 except KeyboardInterrupt:
                    print(Fore.CYAN+"GoodBye")                    
        elif a == "3":#PASSWORD CRACKER
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
                print(Fore.GREEN + "\n\n\nYour pass is: " + Fore.YELLOW + "|--> " +Fore.CYAN+password + Fore.YELLOW + " <--|\n\n\n\n\n" + Fore.GREEN)
            pass 
        elif a == "4": #AREA NUMBER
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            numbers = input(Fore.LIGHTGREEN_EX+"Enter Number\t \nWith code area(+98):\n")
            print(Fore.LIGHTYELLOW_EX+"this number country name is ")
            ph_number = parse(numbers)
            print(geocoder.description_for_number(ph_number,"fa"))
            print("\n\n\n")
        elif a == "5": #CALCULATER
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            num_1 = int(input("Send first number to calc: "))
            num_2 = int(input("Send second number to calc: "))
            action = input(Fore.GREEN+"Which one:"+Fore.CYAN+" *  +  /  - : ")
            if action == "+":
                print(Fore.LIGHTYELLOW_EX+"\n\nYour answer : ")
                print(num_1 + num_2)
                print("\n\n")
            elif action == "-":
                print(Fore.YELLOW+"\n\nYour answer : ")
                print(num_1 - num_2)
                print("\n\n")
            elif action == "*":
                print(Fore.YELLOW+"\n\nYour answer : ")
                print(num_1 * num_2)
                print("\n\n")
            elif action == "/":
                print(Fore.YELLOW+"\n\nYour answer :")
                print(num_1 / num_2)
                print("\n\n")
    except ZeroDivisionError:
        print(Fore.RED+"You can't division by zero ".upper())
    except KeyboardInterrupt:
        print("",flush=True)
        print("GoodBye!",flush=True)
        exit(1)
    else:
        try:
            if a == "6":#####FUN
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
