#              *****T.me/PYTHONTE****** 
#          Owner & compliments : T.me/LooQaat
#  Bug fixes:T.me/HASHIVATOR  ||github.com/Hashivator

from os import system
from lib import handler,lib
from lib.check import *
check_dependency()
check_update()
from colorama import Fore
from lib.banner import *
from lib.colors import c

while True:
    try:
        #HELP MENU
        clear()
        logo()
        Show_menu() 
        operator = input(c.red+" ┌─["+c.lcyan+"Web-Killer"+c.re+"~"+c.lgreen+"@HOME"+c.red+"""]
 └──╼ """+c.green+"$ "+c.pink)             
        if operator == "1": ##DIRECTORY
            handler.directory_Option()
        elif operator == "2":##BITCOIN CHECK
            lib.Bicoin_checker()
        elif operator == "3": 
             handler.network_option()
        elif operator == "9": 
             handler.Developer()
        elif operator == "10": 
            exit(Fore.CYAN+"GoodBye")    
    except KeyboardInterrupt:
          exit(Fore.CYAN+"GoodBye") 
        
   
