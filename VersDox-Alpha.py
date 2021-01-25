import colorama, os, signal, sys, time, platform
from colorama import init, Fore,  Back,  Style

os.system("cls")

init()

so = platform.system()

def inicio():
    if so == "Windows":
        os.system("title VersDoxAlpha - SO = Windows")
    elif so == "Linux":
        os.system("title VersDoxAlpha - SO = Linux")
##########
##inicio##
##########

    os.system("cls")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(Fore.RED + "                                ██╗   ██╗███████╗██████╗ ███████╗██████╗  ██████╗ ██╗  ██╗")
    print(Fore.RED + "                                ██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝")
    print(Fore.RED + "                                ██║   ██║█████╗  ██████╔╝███████╗██║  ██║██║   ██║ ╚███╔╝ ")
    print(Fore.WHITE + "                                ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║  ██║██║   ██║ ██╔██╗ ")
    print(Fore.WHITE + "                                 ╚████╔╝ ███████╗██║  ██║███████║██████╔╝╚██████╔╝██╔╝ ██╗")
    print(Fore.WHITE + "                                  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
    print("                                                          ")
    print(Fore.RED + "                                                  Github:", Fore.WHITE + "@juannicosack")
    print(Fore.RED + "                                                  Youtube:", Fore.WHITE + "Juannicosack")
    print(Fore.RED + "                                                  Discord:", Fore.WHITE + ".gg/7qnpMj3HrY\n")
    print(Fore.WHITE + "                                          https://github.com/juannicosack/VersDox\n\n\n")
    print(Fore.LIGHTCYAN_EX + "                                                   Write help for menu")
    print(Fore.LIGHTCYAN_EX + "                                        Write cls or clear for clear the console")
    print(Fore.LIGHTCYAN_EX + "                                                You are running: " + Fore.RED + so)
    print("")
    print("")
    print("")


def console():
    commands = input(Fore.MAGENTA + "                                                      [root@VersDox]\n                                                           ")
    if commands == "1":
        inicio()
        console()
    elif commands == "help":
        print(Fore.GREEN + "1 => Reiniciar tool")
        print(Fore.RED + "exit => Salir de la tool")
        print(Fore.MAGENTA + "3 => SimpleDoxing")
        print(Fore.YELLOW + "4 => Extradox")
        print(Fore.WHITE + "5 => IpLogger")
        print(Fore.CYAN + "6 => Limpiar pantalla")
        console()
    elif commands == "exit":
        print(Fore.YELLOW + "[root@VersDox] Saliendo de la tool...")
        time.sleep(0.50)
        if so == "Windows":
            os.system("cls")
        elif so == "Linux":
            os.system("clear")    
        os.system("exit")
    elif commands == "3":
        dox = input("                                                  A quien quieres doxear? ")
        os.system("python extras/sherlock " + dox)
    elif commands == "4":
        os.system("python extras/extradox.py")
    elif commands == "5":
        os.system("start https://iplogger.org/es/")
        print("https://iplogger.org/es/ => Creador de IpLogger\n")
        os.system("start https://grabify.link/")
        print("https://grabify.link/ => Creador de IpLogger X2\n")
        os.system("start https://www.ultratools.com/tools/geoIp")
        print("https://www.ultratools.com/tools/geoIp => GeoIP\n")
        console()
    elif commands == "6":
        if so == "Windows":
            os.system("cls")
        elif so == "Linux":
            os.system("clear")    
        inicio()
        console()
    elif commands == "cls":
        os.system("cls")
        inicio()
        console()
    elif commands == "clear":
        os.system("clear")    

inicio()
console()
