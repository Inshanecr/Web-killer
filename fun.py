#******T.me/PYTHONTE******** 
#Owner
#--‐---------------T.me/LooQaat------------------
#Bug fixes and complements
#‐-----------------T.me/HASHIVATOR----------
from requests import get
from ipapi import location
from random import sample
from colorama import Fore
from phonenumbers import geocoder, parse
from datetime import datetime
from itertools import count
from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p

all = l + u + d + p
    

class Style:
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'


# print(f"\ndate : {datetime.now()}")
# print(Fore.RED + "[1] " + Fore.GREEN + "Show your ip [ Use vpn ]")
# print(Fore.RED +"[2] " + Fore.GREEN + "Password cracker")
# print(Fore.RED + "[3] " + Fore.YELLOW + "Show your Area Number: ")
# print(Fore.RED + "[4] " + Fore.YELLOW + "Calculate number")
# print(Fore.RED + "[5] " + Fore.GREEN + "Fun")

ok = True
while True:

    
    try:
        print("""_   _    _    ____  _   _ _____     ___  _____ ___  ____  
| | | |  / \  / ___|| | | |_ _\ \   / / \|_   _/ _ \|  _ \ 
| |_| | / _ \ \___ \| |_| || | \ \ / / _ \ | || | | | |_) |
|  _  |/ ___ \ ___) |  _  || |  \ V / ___ \| || |_| |  _ < 
|_| |_/_/   \_\____/|_| |_|___|  \_/_/   \_\_| \___/|_| \_\
""")
        print(Fore.RESET + f"\ndate : {datetime.now()}\r")
        print(Fore.RED + "[1] " + Fore.YELLOW + "Show your ip " + Fore.GREEN + "[ Use vpn ]")
        print(Fore.RESET + Fore.RED +"[2] " + Fore.YELLOW + "Password Generator")
        print(Fore.RED + "[3] " + Fore.YELLOW + "Show your Area Number ")
        print(Fore.RED + "[4] " + Fore.YELLOW + "Calculate number")
        print(Fore.RED + "[5] " + Fore.YELLOW + "Fun")
        print("")
        a = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX)
        print(Fore.RESET)
        if a == "1":
            ip = get("https://api.ipify.org").text
            print('\n' + Fore.MAGENTA + ip + Fore.RESET)
            http = get("https://api.ipify.org").text
            cou = location(http)["country"]
            if cou == "IR":
                print(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + Style.BOLD + "BLOCKED" + Style.END + " from server  " + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Iranian"+ Fore.WHITE +" IP " + Style.UNDERLINE + Fore.GREEN + cou + Style.END + Fore.RESET)
                
        elif a == "2":
            try:
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
        elif a == "3":
            numbers = input("Enter Number\t \nWith code area(+98):")
            ph_number = parse(numbers)
            print(geocoder.description_for_number(ph_number,"fa"))
        elif a == "4":
            print("""------------------------T.me/LooQaat--------------------""")
            num_1 = int(input("Send first number to calc: "))
            num_2 = int(input("Send second number to calc: "))
            action = input("Which one: * + / - : ")
            if action == "+":
                print(num_1 + num_2)
            elif action == "-":
                print(num_1 - num_2)
            elif action == "*":
                print(num_1 * num_2)
            elif action == "/":
                print(num_1 / num_2)
    except KeyboardInterrupt:
        print("",flush=True)
        print("GoodBye!",flush=True)
        exit(1)
    else:
        try:
            if a == "5":
                for i in count(2,2):
                    if i == 198618:
                        break
                    else:
                        print(i)
        except(RuntimeError,KeyboardInterrupt):
            print(" ", end="", flush=True)
            continue
