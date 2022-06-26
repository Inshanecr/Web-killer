from lib.directories import directorylist,wordpress_dir,admin_finder
from requests import get
from colorama import Fore
from ipapi import location
from time import sleep
from lib.check import clear
from lib.colors import c
from lib import banner
from urllib3 import PoolManager

manager = PoolManager()


def check_clear_log_file(path_check_file=""):
   with open(f"log/{path_check_file}.log","w+") as clear_log:
       clear_log.write("")

def User_Valid(url):
        if url == "":
           print(Fore.RED+"\nplease Enter Url")
           sleep(1)
           return "continue"
       # elif not "https://" or "http://" in url:
          #   print(c.pink+"\n please Write URL  With out https:// ")
          #   sleep(2)
       #      return "continue"  

           
def continue_process():
            nun = input(c.green+"\nDo You Want To Back menu > Y/N :").upper()
            if nun == "Y":
                  return "break"
            else:
                  pass
  
def Directory_search(status="",msg="",path_log="",banner_name=""):
      try:
       while True:
           clear()
           banner.Dir_Option_banner(method_name=banner_name)
           print("\n               -----T.ME/HASHIVATOR || T.me/LooQaat------\n")
           sleep(0.5)
           check_clear_log_file(path_check_file=path_log)
           print(c.yellow+f"\n             [ ▪︎ ] Please wait\nwhile all the results are saved in > log/{path_log}.log \n         This will take a {msg}\n"+c.re)
           
           
           url= "https://"+input(Fore.GREEN+"\nEnter the URL"+Fore.LIGHTRED_EX+" [with out https://] : "+c.pink).lower()+"/"
           
           valid = User_Valid(url=url)
           if valid == "continue":
               continue
                   
                   
           if status == "wordpress":
             s = get("http://"+url+"/wp-content/plugins/")
             if s.status_code == 404 or s.status_code == 500:
                  print(Fore.RED+" [ ! ] "+Fore.YELLOW+"Site NOT Wordpress")
                  sleep(4)
                  continue
             else:
                 data = wordpress_dir
                 
           elif status  == "AllDirectory":
              data = directorylist
              
           elif status == "php":
             data  = directorylist[829:9735]
             
           elif status == "adminfinder":
              data = admin_finder
              
              
           for i in data: 
              h = manager.request('GET',url+i)
              
              if h.status == 200:            
                    with open(f"log/{path_log}.log","a+") as log:      
                      log.write(str(url+i+"\n"))
                      
           print(c.lcyan+"\n[ * ] Please check result in Dir/result.log ")
           
           if_exit = continue_process()
           if if_exit == "break":
              break

             
      except Exception as Ex:
               print(Ex)
               sleep(10)
               print(Fore.RED+"[-]"+Fore.YELLOW+"Your URL ISN'T CORRECT\n")
               
      except KeyboardInterrupt:
               exit(Fore.CYAN+"\nGoodBye")
      
def Bicoin_checker():
           while True:
                clear()
                banner.bitcoin_check_banner()
                print("-----T.ME/HASHIVATOR----T.me/LooQaat------")
                wallet = input(Fore.CYAN+"\nSend your bitcoin wallet address please: \n")
                wallet_ceck = get("https://blockchain.com/btc/address"+wallet)
                if wallet_ceck.status_code == 200:
                   print(f"Your wallet address is correct :\n {Wallet}\n")
                else:
                    print(Fore.RED+"\n[ - ] wrong Wallet ! ! !\n") 
                    sleep(1)
                if_exit = continue_process()
                if if_exit == "break":
                    break
                  
                  
                  
                  
def ip_info():
    clear()
    banner.network_banner(method_name="ip")
    banner.terminal_Logo("Network/IP")
    b = c.blue
    gy = c.red
    g = c.green
    http = get("https://api.ipify.org").text
    source = location(http)
    ban  = (f"""
{g}  [ ! ]︎{c.grey}See your ip information\n
     {g}[❤︎]{b} ip :{gy} {source["ip"]}
     {g}[❤︎]{b} city :{gy} {source["city"]}
     {g}[❤︎]{b} region :{gy} {source["region"]}
     {g}[❤︎]{b} id country :{gy} {source["country"]}
     {g}[❤︎]{b} country :{gy} {source["country_name"]}
     {g}[❤︎]{b} Calling Code :{gy} {source["country_calling_code"]}
     {g}[❤︎]{b} Languages :{gy} {source["languages"]}
     {g}[❤︎]{b} org :{gy} {source["org"]}        """)
    for line in ban.split("\n"):
       sleep(0.1)
       print(line)
    input(c.cyan+"\n        [ ○ ] Press Enter To Return Menu ")



def HttpHeader():
        while True:
          try:
                clear()
                banner.network_banner(method_name="http")
                print(Fore.LIGHTRED_EX+" [ - ] Enter The Domain\n")
                inp = banner.terminal_logo("Network/Header")    
                
                Valid_Url = User_Valid(url=inp)
                if Valid_Url == "continue":
                   continue
                else:
                  result = get('https://api.hackertarget.com/httpheaders/?q=' + inp).text
                  print(c.pink+"Your result  > ")
                  print("\n"+Fore.LIGHTBLUE_EX+result)
                  sleep(1)
                  if_exit = continue_process()
                  if if_exit == "break":
                     break
          except KeyboardInterrupt:
            exit(Fore.CYAN+"\nGoodBye :)")
            
            
def ShareDns():
       while True:
           try:
                clear()
                banner.network_banner(method_name="shareDns")
                print(Fore.RED+"\n [ ! ] Plase Enter IP/Domain "+c.yellow+"[with out https://]: \n")
                #command banner
                inp = banner.terminal_logo("Network/ShareDns")
                
                Valid_Url = User_Valid(url=inp)
                if Valid_Url == "continue":
                   continue
                else:   
                  result =get('https://api.hackertarget.com/findshareddns/?q=' + inp).text
                  print("\n"+Fore.LIGHTBLUE_EX+result) 
                  sleep(1)
                  if_exit = continue_process()
                  if if_exit == "break":
                     break
           except KeyboardInterrupt:
            exit(Fore.CYAN+"\nGoodBye :)")


### DNS LOOK UP
def DnsLookUp():
        while True:
           try:
                clear()
                banner.network_banner(method_name="DnsLookUp")
                print(Fore.RED+" [!] Enter The Domain\n"+c.yellow+"[with out https://]: ")
                #command banner
                inp = banner.terminal_logo("Network/DnsLookUp") 
                
                Valid_Url = User_Valid(url=inp)
                if Valid_Url == "continue":
                   continue
                else:
                  result = get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
                  print("\n"+Fore.LIGHTBLUE_EX+result)
                  sleep(1) 
                  if_exit = continue_process()
                  if if_exit == "break":
                    break
           except KeyboardInterrupt:
            exit(Fore.CYAN+"\nGoodBye :)")
