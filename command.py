#LIBARIES
from os import system 
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


all = l + u + d + p

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
              Back_menu()
       except Exception as Ex:
               print(Fore.RED+"[-]"+Fore.YELLOW+"Your URL ISN'T CORRECT\n")
               
       except KeyboardInterrupt:
               exit(Fore.CYAN+"\nGoodBye")
      
def Bicoin_checker():
            print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
            ip = get("https://api.ipify.org").text
            print('\n' + Fore.MAGENTA + ip + Fore.RESET)
            http = get("https://api.ipify.org").text
            cou = location(http)["country"]
            if cou == "IR":
                exit(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + "BLOCKED from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " +Fore.GREEN + cou +"\n\n\n\n"+Fore.RESET)
            else:
                wallet = input(Fore.CYAN+"\nSend your bitcoin wallet address please: \n")
                wallet_ceck = get("https://blockchain.com/btc/address"+wallet)
                if wallet_ceck.status_code == 200:
                   print(f"Your wallet address is correct :\n {Wallet}\n")
                else:
                    print(Fore.RED+"\n[-]wrong Wallet ! ! !\n") 
                    sleep(1)
                Back_menu()
                 

def Password_generator():
  while True:
    try:
         print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
         length = int(input("Enter length of password: "))   
    except ValueError:
        print("Length can't be string or float or empty ...")   
        sleep(5)        
    ok = True
    if length < 5 or length > 120:
        print(Fore.RED+"\n[ * ] Password length must be between 8 and 100!\n")
        sleep(4)
        break             
    elif ok == True:
        password = "".join(sample(all,length))
        print(Fore.GREEN + "\n\nYour pass is: " + Fore.YELLOW + "|--> " +Fore.CYAN+password + Fore.YELLOW + " <--|\n" + Fore.GREEN)
        Back_menu()    
                                     
