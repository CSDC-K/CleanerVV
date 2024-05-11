#//MADE BY VV || VrOlsn
import json
import os
import time
import re
import sys
import inquirer as iq
from InquirerPy import prompt, inquirer
from InquirerPy.separator import Separator
import os
import pystyle
from pystyle import Write, Colors
import ctypes


mascii = """

                                          _    _ _    _                            
                                           \  /   \  /                             
                                            \/     \/                              
                                                                                
                 _____   _____  _______ _____ _______ _____ ______ _______  ______
                |     | |_____]    |      |   |  |  |   |    ____/ |______ |_____/
                |_____| |          |    __|__ |  |  | __|__ /_____ |______ |    \_
                                                                                
                

                                                                        -Made By VrOlsn


                -1.2
"""



RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clstart():

    import shutil
    import subprocess


    tmmp = "TEMP NOT DELETED"
    tmps = "NOT DELETED"
    stup = "NOT DELETED"
    sftdis = "SOFTWAREDISTRIBUTION NOT DELETED"
    dnsf = "NOT FLUSHED"


    config_file_path = "config.json"
    with open(config_file_path) as f:
        config_data = json.load(f)

    if config_data.get("Temp") == True:
    
        Write.Print("\n[...]", Colors.yellow, interval=0)
        Write.Print("Temp Deleting...\n", Colors.white, interval=0)
        time.sleep(2)

        local_app_data = os.environ.get('LOCALAPPDATA')
        temp_path = os.path.join(local_app_data, 'Temp')

        for root, dirs, files in os.walk(temp_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass

        Write.Print("[+]", Colors.light_green, interval=0)
        Write.Print("Temp Succesfuly Deleted.\n", Colors.white, interval=0)
        time.sleep(2)

        tmmp = "TEMP DELETED"

    if config_data.get("%Temp%") == True:
        import shutil


        Write.Print("\n[...]", Colors.yellow, interval=0)
        Write.Print("Windows Temp Deleting...\n", Colors.white, interval=0)
        time.sleep(2)

        tmp = os.environ.get('TEMP')

        for root, dirs, files in os.walk(tmp):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass

        Write.Print("[+]", Colors.light_green, interval=0)
        Write.Print("Windows Temp Succesfuly Deleted.\n", Colors.white, interval=0)
        time.sleep(1)

        tmps = "WINDOWS TEMP DELETED"
    if config_data.get("Startup") == True:

        Write.Print("\n[...]", Colors.yellow, interval=0)
        Write.Print("Startup Deleting...\n", Colors.white, interval=0)
        time.sleep(2)

        startup_folder_path = os.path.join(os.environ.get('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        for root, dirs, files in os.walk(startup_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass

        Write.Print("[+]", Colors.light_green, interval=0)
        Write.Print("Startup Succesfuly Deleted.\n", Colors.white, interval=0)
        time.sleep(2)

        stup = "STARTUP DELETED"


    if config_data.get("SoftwareDistribution") == True:

        Write.Print("\n[...]", Colors.yellow, interval=0)
        Write.Print("Sofware Distribution Deleting...\n", Colors.white, interval=0)

        time.sleep(2)
        software_distribution_path = os.path.join(os.environ.get('WINDIR'), 'SoftwareDistribution')

        for root, dirs, files in os.walk(software_distribution_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass

        Write.Print("[+]", Colors.light_green, interval=0)
        Write.Print("Software Distribution Succesfuly Deleted.\n", Colors.white, interval=0)
        time.sleep(2)

        sftdis = "SOFTWAREDISTRIBUTION DELETED"


    if config_data.get("ipconfig /flushdns") == True:

        Write.Print("\n[...]", Colors.yellow, interval=0)
        Write.Print("Flushing Dns...\n", Colors.white, interval=0)
        time.sleep(2)

        subprocess.run(["ipconfig", "/flushdns"], check=True)

        Write.Print("[+]", Colors.light_green, interval=0)
        Write.Print("Dns Succesfuly Flushed..\n", Colors.white, interval=0)
        time.sleep(2)

        dnsf = " DNS FLUSHED"

    logs = open("LOG.txt", "w")

    import datetime

    current_datetime = datetime.datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    hour = current_datetime.hour
    minute = current_datetime.minute
    log_content = f"{year}:{month}:{day} || {hour}:{minute}\n\n\n         INTERACTIVES        \n\n        -{dnsf}\n        -{tmmp}\n        -{tmps}\n        -{sftdis}\n        -{stup}\n\n        LATEST CLEAN LOG\n\n"

    logs.write(log_content)

    Write.Print("[+]", Colors.light_green, interval=0)
    Write.Print("Latest Clean Logs In LOG.txt\n", Colors.white, interval=0)
    time.sleep(3)

    logs.close()

    mainmenu()



def drupdate():
    pass


def optscreen():
    import inquirer
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    os.system("cls")

    questions = [
        inquirer.Checkbox('Options',
                        message=f"{BLUE}Tick to needed cleans for Directorys{RESET}",
                        choices=[
                            (f"{CYAN}Temp{RESET}", 'Temp'),
                            (f"{CYAN}%Temp%{RESET}", '%Temp%'),
                            (f"{CYAN}Startup{RESET}", 'Startup'),
                            (f"{CYAN}SoftwareDistribution{RESET}", 'SoftwareDistribution'),
                            (f"{CYAN}ipconfig /flushdns{RESET}", 'ipconfig /flushdns'),
                        ],
                        
        ),
    ]
    answers = inquirer.prompt(questions)

    all_choices = ['Temp', '%Temp%', 'Startup', 'SoftwareDistribution', 'ipconfig /flushdns']

    selected_options = answers['Options']
    
    config = {}
    for choice in all_choices:
        config[choice] = choice in selected_options
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    Write.Print("[+]", Colors.light_green, interval=0)
    Write.Print("Configs saved succesfuly!", Colors.white, interval=0)
    time.sleep(1.5)
    mainmenu()


    
def credits():
    
    print("""
          
               DEVELOPED BY PYTHON
    
                Coded By VrOlsn

                Shared By VrOlsn

        Company: VV
    
    """)

    print("Press enter to continue")
    input()
    mainmenu()



def mainmenu():

    os.system("cls")

    print(mascii)


    line = "=" * 35

    menu_choices = [
        Separator(line=line),
        '1>           Start Clean',
        '2>           Drivers (SOON)',
        '3>           Options',
        '4>           Credits',
        Separator(line=line),
        '4>             Exit'
    ]
    res = inquirer.select(
    message=f"\nUse arrow keys to select and ENTER to confirm\nPlease select an option\n\n ~Made By Kc~:",
    choices=menu_choices,
    default=menu_choices[0],
    pointer='=>',
    qmark='').execute()


    if res == menu_choices[1]:
        clstart()

    if res == menu_choices[2]:
        drupdate()

    if res == menu_choices[3]:
        optscreen()

    if res == menu_choices[4]:
        credits()

    if res == menu_choices[5]:
        exit

if __name__ == "__main__":
    mainmenu()
