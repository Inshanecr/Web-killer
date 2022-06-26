from os import system
import platform
import json
from lib.colors import c

def clear():
 if platform.uname()[0] == "Windows":
    system("cls")
 else:
    system("clear")


def check_dependency():
  try: 
    from colorama import Fore
    import ipapi,requests
  except ImportError:
    exit("please run install Libraries\ncommand => python3 -m pip install -r requirements.txt")
    
    
  http = requests.get("https://api.ipify.org").text
  cou = ipapi.location(http)["country"]
  if cou == "IR":
    exit(Fore.LIGHTBLACK_EX + "Your IP has " + Fore.LIGHTRED_EX + "BLOCKED from server" + Fore.LIGHTBLUE_EX + "[ Turn on VPN ] " + Fore.RESET + '|' + Fore.RED + " Your country "+ Fore.WHITE +" ↬ " +Fore.GREEN + cou +"\n\n\n\n"+Fore.RESET)
   

def check_update():
    import requests
    http = requests.get("https://raw.githubusercontent.com/Inshanecr/Web-killer/main/setting.json").text
    http_json = json.loads(http)
    with open("setting.json", "r") as version:
        data = json.load(version)
        if data['version'] < http_json['version']:      
           exit(c.red+"["+c.re+"*"+c.red+"] Please Update Tool\n"+c.yellow+"Commands => "+c.pink+"cd ..\nrm -r Web-killer\ngit clone https://github.com/inshanecr/Web-killer\ncd Web-killer\npython main.py")