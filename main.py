#              *****T.me/PYTHONTE****** 
#          Owner & compliments : T.me/LooQaat
#  Bug fixes:T.me/HASHIVATOR  ||github.com/Hashivator


from os import system
try: 
 from colorama import Fore
 from string import ascii_lowercase as l, ascii_uppercase as u, digits as d, punctuation as p
 from directories import directorylist
 from banner import *
 from command import *
except ImportError:
    exit("please run install Libraries\ncommand => python3 -m pip install -r requirements.txt")

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
            
    except KeyboardInterrupt:
          exit(Fore.CYAN+"GoodBye") 
        
   
