#******T.me/PYTHONTE******** 
#Owner: T.me/LooQaat-
#Bug fixes:T.me/HASHIVATOR
#compliments: T.me/LooQaat


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
        exit("please install library \ncommand > python3 -m pip install -r [library]\nLibraries => pip install colorama\npip install time \npip install datetime")
After_ip_Click()
all = l + u + d + p


while True:
    try:
        #HELP MENU
        Show_menu()
        a = input(Fore.CYAN + "Which tools you need: " + Fore.LIGHTMAGENTA_EX)
        print(Fore.RESET)   
        if a == "1": ##DIRECTORY
            Directory_search(data=directorylist)
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
   
