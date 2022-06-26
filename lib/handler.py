from lib.colors import c
from time import sleep 
from lib import check,banner,lib

red = c.red
g = c.green
ye = c.yellow
cy = c.cyan
b = c.blue

def network_option():
  while True:
    check.clear()
    banner.network_banner(method_name="main")
    banner.netwok_banneMr() 
    result = banner.terminal_logo("Network")
    if result == "1":
        lib.ip_info()
    elif result == "2":
        lib.HttpHeader()
    elif result == "3": 
      lib.ShareDns()
    elif result == "4":
      lib.DnsLookUp()    
    elif result == "5":  
      break  
      
        
def Developer():
    check.clear()
    ban =(f"""{cy}
         _   _               _                       _              
        ( ) ( )             ( )     _               ( )_            
        | |_| |   _ _   ___ | |__  (_) _   _    _ _ | ,_)   _    ___
        |  _  | /'_` )/',__)|  _ `\| |( ) ( ) /'_` )| |   /'_`\ ( '__)
        | | | |( (_| |\__, \| | | || || \_/ |( (_| || |_ ( (_) )| | 
        (_) (_)`\__,_)(____/(_) (_)(_)`\___/'`\__,_)`\__)`\___/'(_) 

{red}[•]{g} Develpers :{ye} 𝙷𝚊𝚜𝚑𝚒𝚟𝚊𝚝𝚘𝚛 𝚃𝚎𝚊𝚖

{red}[•]{g} 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 :{ye} 𝚃.𝚖𝚎/𝙷𝚊𝚜𝚑𝚒𝚟𝚊𝚝𝚘𝚛{b} |{ye} 𝚃.𝚖𝚎/𝙻𝚘𝚘𝚀𝚊𝚊𝚝

{red}[•]{g} 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 :{ye} 𝚃.𝚖𝚎/𝚙𝚢𝚝𝚑𝚘𝚗𝚝𝚎
  """)
    banner.print_slow(banner=ban)
    input(c.cyan+"\n        [ ○ ] Press Enter To Return Menu ")



def directory_Option():
 while True:
    clear()
    banner.Dir_Option_banner(method_name="main")
    banner.directory_banner()
    result = banner.terminal_logo("Directory")
    if result == "1":
        lib.Directory_search(
              status="AllDirectory",
                msg="Two Hours",
                  path_log="AllDirectory",
                    banner_name="All")
        
    elif result == "2":
        lib.Directory_search(
            status="php",
              msg="One Hours",
                path_log="phpDir",
                    banner_name="php")
              
    elif result == "3": 
        lib.Directory_search(
           status="adminfinder",
              msg="20 Minutes",
                path_log="adminDir",
                    banner_name = "admin")
              
    elif result == "4":  
        lib.Directory_search(
            status="wordpress",
              msg="40 Mminutes",
                path_log = "wordpressDir",
                    banner_name = "wordpress")
              
              
    elif result == "5":  
        break
        
