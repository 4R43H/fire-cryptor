''' 
Developer ==> arash kiani
Email ==> arashkianidev@gmail.com

Version => 1.0 , 2022

#MadeIniran

    ______ _            ______                             _             
    |  ____(_)          |  ____|                           | |            
    | |__   _ _ __ ___  | |__   _ __   ___ _ __ _   _ _ __ | |_ ___  _ __ 
    |  __| | | '__/ _ \ |  __| | '_ \ / __| '__| | | | '_ \| __/ _ \| '__|
    | |    | | | |  __/ | |____| | | | (__| |  | |_| | |_) | || (_) | |   
    |_|    |_|_|  \___| |______|_| |_|\___|_|   \__, | .__/ \__\___/|_|   
                                                __/ | |                  
                                                |___/|_|                  

                                                        Base64 | Hex | rot13 


'''

from colorama import Fore as color
from time import sleep
import os, sys
import myClasses, banner, decoder


bold = '\033[1m'
endbold = '\033[0m'


def needs(module):
    module = str(module);os.system('clear')
    print(color.GREEN+"Please install% library\n pip3 install %s" %(module))
    sleep(0.3);sys.exit()


try:
    from colorama import Fore as color
except:
    needs(colorama)


myClasses.Introduce()


while True:
    os.system('clear')
    try:
        banner.banner();banner.menu()
        option = int(input(color.RED+"\n[⚡] "+color.RED+"fire cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " ))
        
        
        if (option == 1):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"fire cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t ")
            os.system(f'echo {user_option} | base64')
            input('\n press any key...'+endbold)
            continue
        
        elif (option == 2):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"fire cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"hex"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | xxd -p")
            input('\n press any key...'+endbold)
            continue
        elif (option == 3):
            os.system('clear');banner.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"fire cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"rot13"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            
            input('\n press any key...'+endbold)
            continue

        
        
        elif (option == 4):
            os.system('clear');banner.banner();banner.decoder_menu()
            option = int(input(color.RED+"\n[⚡] "+color.RED+"fire cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTRED_EX+" ⇒ " ))
            decoder.decoder_menu(option)
            continue
            
        elif (option == 0):
            os.system('clear')
            sys.exit()


    except KeyboardInterrupt:
        sys.exit()
