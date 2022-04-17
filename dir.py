#******T.me/PYTHONTE******** 
#Owner T.me/LooQaat-
#AUTHR T.me/HASHIVATOR
#Bug fixes and complements
#‐-----------------T.me/HASHIVATOR

#installing
from os import system
#print("INSTSLLING  DOCUMENT\n\n\n\n\n\n\n ")
#system("pip install requests")  
#system("pip install phonenumbers")  
#system("pip install ipapi")  
#system("pip install colorama") 
#system("pip install itertools")  
#system("pip install datetime")
#system("clear")
#libaries
system("clear")
try: 
 from colorama import Fore
 from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
 from directories import directorylist
 from banner import *
 from command import *
except ImportError:
        exit(Fore.RED+"please install library \ncommand > python3 -m pip install -r [library]\n"+Fore.YELLOW+"Libraries => "+"pip install requests\npip install phonenumbers\npip install ipapi\npip install colorama\npip install itertools\npip install datetime")

all = l + u + d + p
while True:
    try:
        #HELP MENU
        Show_menu()
        a = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX)
        print(Fore.RESET)   
        if a == "1": ##DIRECTORY
            Directory_search()
        elif a == "2":##BITCOIN CHECK
            Bicoin_checker()                         
        elif a == "3":#PASSWORD GENERATOR 
            Password_generator()
        elif a == "4": #AREA NUMBER
            Area_number()
        elif a == "5": #CALCULATER
            Calculator()
    except KeyboardInterrupt:
          exit(Fore.CYAN+"GoodBye") 
    continue        
   
