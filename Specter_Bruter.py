# Made by matxd -> t.me/matxd1337

from colorama import Fore , init ; init()
from random import choices
from requests import get
from pystyle import System

System.Title("~~ Specter Bruter ~~")

base_url = "https://pst.klgrth.io/paste/"

ascii = """

███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗       ██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗      ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝█████╗██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗╚════╝██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗
███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║      ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                 
"""

def Main():

    print(ascii.replace('█' , Fore.MAGENTA+'█'+Fore.RESET))
    print(f"[{Fore.MAGENTA}!{Fore.RESET}] Press Enter for lauch the bruter") 

    input()

    System.Clear()
    print(ascii.replace('█' , Fore.MAGENTA+'█'+Fore.RESET))

    while True :

        chars = "abcdefghijklmnopqrstuvwyz0123456789"
        code = choices(chars , k=5)
        key = ''.join(code)
        url = base_url+key

        r = get(url).status_code

        if r == 200 :
            print(f"[{Fore.GREEN}+{Fore.RESET}] {url} -> HIT")
            open('hits.txt', 'a+').write(url + '\n')
        if r == 404 :
            print(f"[{Fore.RED}+{Fore.RESET}] {url} -> BAD")
            open('hits.txt', 'a+').write(url + '\n')


Main()