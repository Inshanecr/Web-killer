#              *****T.me/PYTHONTE****** 
#          Owner & compliments : T.me/LooQaat
#  Bug fixes:T.me/HASHIVATOR  ||github.com/Hashivator

#libaries
from os import system
system("clear")
try: 
 from colorama import Fore
 from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
 from directories import directorylist
 from banner import *
 from command import *
except ImportError:
    print("waiting for installing libaries ...\n\n")
    system("pip install colorama")
    system("pip install requests")
    system("pip install ipapi")
    system("pip install phonenumbers")
    exit("please run script again")

#After_ip_Click()
all = l + u + d + p

while True:
    try:
        #HELP MENU
        system("clear")
        Show_menu()      
        operator = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX+Fore.RESET)           
        if operator == "1": ##DIRECTORY
            Directory_search(data=directorylist)
        elif operator == "2":##BITCOIN CHECK
            Bicoin_checker()                         
        elif operator == "3":#PASSWORD GENERATOR 
            Password_generator()
        elif operator == "4": #AREA NUMBER
            Area_number()
        elif operator == "5":
            Calculator()
    except KeyboardInterrupt:
          exit(Fore.CYAN+"GoodBye") 
    continue        
   
