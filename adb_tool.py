import os
import re
import subprocess as sp
from time import sleep


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Bold Text Colors
    bd_dark_Gray = '\033[1;30;40m'
    bd_bright_Red = '\033[1;31;40m'
    bd_bright_Green = '\033[1;32;40m'
    bd_yellow = '\033[1;33;40m'
    bd_bright_Blue = '\033[1;34;40m'
    bd_bright_Magenta = '\033[1;35;40m'
    bd_bright_Cyan = '\033[1;36;40m'
    bd_white = '\033[1;37;40m'

    # Text Color Grey Background
    txt_black = '\033[0;30;47m'
    txt_red = '\033[0;31;47m'
    txt_green = '\033[0;32;47m'
    txt_brown = '\033[0;33;47m'
    txt_blue = '\033[0;34;47m'
    txt_magenta = '\033[0;35;47m'
    txt_cyan = '\033[0;36;47m'
    txt_light_Grey = '\033[0;37;40m'

    # Colored Background
    bg_black = '\033[0;37;48m'
    bg_red = '\033[0;37;41m'
    bg_green = '\033[0;37;42m'
    bg_yellow = '\033[0;37;43m'
    bg_blue = '\033[0;37;44m'
    bg_magenta = '\033[0;37;45m'
    bg_cyan = '\033[0;37;46m'
    bg_white = '\033[0;37;47m'


class ConnectWifi(Color):
    port = 5555
    adb_ui = '''
        
        .----------------.  .----------------.  .----------------.
        | .--------------. || .--------------. || .--------------. |
        | |      __      | || |  ________    | || |   ______     | |
        | |     /  \     | || | |_   ___ `.  | || |  |_   _ \    | |
        | |    / /\ \    | || |   | |   `. \ | || |    | |_) |   | |
        | |   / ____ \   | || |   | |    | | | || |    |  __'.   | |
        | | _/ /    \ \_ | || |  _| |___.' / | || |   _| |__) |  | |
        | ||____|  |____|| || | |________.'  | || |  |_______/   | |
        | |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'

    '''

    def __init__(self):
        os.system("cls")
        os.system("color 0a")
        os.system("mode 80,35")
        os.system('title Setup ADB Tools [ V 1.0.0 ]')
        self.show_ui()
        self.main_menu()
        # self.choices()

    def show_ui(self):
        print(f"{self.bd_bright_Cyan}")
        show_t = '''
                        ***********************
                        *****             *****
                        * Welcome Everybody:] *
                        *****             *****
                        ***********************

        .----------------.  .----------------.  .----------------.
        | .--------------. || .--------------. || .--------------. |
        | |      __      | || |  ________    | || |   ______     | |
        | |     /  \     | || | |_   ___ `.  | || |  |_   _ \    | |
        | |    / /\ \    | || |   | |   `. \ | || |    | |_) |   | |
        | |   / ____ \   | || |   | |    | | | || |    |  __'.   | |
        | | _/ /    \ \_ | || |  _| |___.' / | || |   _| |__) |  | |
        | ||____|  |____|| || | |________.'  | || |  |_______/   | |
        | |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'

           *****************************************************
           ****          Setup Android Tool @v1.0.0         ****
           ****        Developed by : Sherien Bassem        ****
           ****               Ghana-Est Company             ****
           *****************************************************
                            ******************
                            **** Remember ****
                            ******************

                - Enable [USB debugging] on your Android Device
                - No Need Root Permission!
        '''
        print(show_t)
        input("                 press enter key to continue ....")

    def main_menu(self):
        os.system("cls")
        os.system('title Setup ADB Tools [ V 1.0.0 ] - Connect Options')
        menu = '''
            = #################################################### =
            = ####          Choose the order you need         #### =
            = #################################################### =
            = ####   [1] wi-fi - Connecting to your device    #### =
            = ####   [2] Exit  - to exit from Tool            #### =
            = #################################################### =
        '''
        print(menu)
        print("")
        self.choices()
        # input("                 press any key to exit ....")

    def choices(self):
        user_choice = input("Enter Your Choice: ")
        try:
            uc = int(user_choice)
            if uc == 1:
                print("")
                self.wifi_connection()
            elif uc == 2:
                print("")
                self.message("The tool will be finished")
                sleep(3)
                exit()
            else:
                err_1 = '''
                *******************************************
                *** Please Choose Number [ 1 ] or [ 2 ] ***
                *******************************************
                '''
                print(err_1)
                sleep(3)
                self.main_menu()
        except ValueError:
            err_2 = '''
                *****************************************
                ***  Please Enter A Valid Number !!!  ***
                *****************************************
            '''
            print(err_2)
            sleep(3)
            self.main_menu()

    def validate_ip(self, ip):
        self.is_ip = re.search(
            # r"^\d{3}\.\d{3}\.\d\.\d{3}$", self.ip_address)
            r"^\d{3}\.\d{3}\.\d\.(\d|\d{2}|\d{3})$", ip)
        if self.is_ip:
            return True
        else:
            self.message("Pleas Insert A Valid Ip-Address")
            sleep(5)
            print(" ")
            self.main_menu()

    def wifi_connection(self):
        print("")
        device_ip = input("Enter Your Device ip: ")
        cmd = f"adb connect {device_ip}:{self.port}"
        v_ip = self.validate_ip(device_ip)
        if v_ip:
            self.run_cmd(cmd)

    def run_cmd(self, cmd):
        try:
            proc = sp.run(cmd, shell=True, check=True, capture_output=True)
            out = proc.stdout.decode("utf-8")
            if out.startswith('cannot'):
                raise Exception()
            else:
                self.message(out)
                sleep(5)
                self.next_menu()
                print(f"{self.bg_black}")
                os.system("cls")
        except sp.CalledProcessError as error:
            out = error.stderr.decode("utf-8")
            self.message(f'\n\nError : {out}')
            self.main_menu()
        except:
            # print("Your Device Is Not Found")
            self.message("Your Device Is Not Found")
            sleep(3)
            self.main_menu()

    def message(self, msg):
        msg_txt = f'''
        ****************************************************
                {msg}
        ****************************************************

        '''
        print(msg_txt)

    def next_menu(self):
        print("")
        menu_n = '''
        = #################################################### =
        = ####          Choose the order you need         #### =
        = #################################################### =
        = ####   [1] Android adb install backages         #### =
        = ####   [2] Fire-Stick adb Add Arabic Language   #### =
        = ####   [3] Go To Main Menu                      #### =
        = ####   [4] Exit - to exit from Tool             #### =
        = #################################################### =
        '''
        os.system("cls")
        os.system('title Setup ADB Tools [ V 1.0.0 ] - install options')
        print(menu_n)
        self.install_choices()
        # sleep(5)

    def install_choices(self):
        user_choice = input("Enter Your Choice: ")
        try:
            uc = int(user_choice)
            if uc == 1:
                print("")
                # print("1")
                self.nested_menu()
                print("")

            elif uc == 2:
                print("")
                self.lang_fire_cmd()
                sleep(2)

            elif uc == 3:
                print("")
                self.main_menu()
                sleep(2)
            elif uc == 4:
                self.message("The tool will be finished")
                exit()
            else:
                err_1 = '''
                ********************************************
                *** Please Choose Number [ 1, 2, 3 or 4] ***
                ********************************************
                '''
                print(err_1)
                sleep(3)
                self.next_menu()
                self.install_choices()
        except ValueError:
            err_2 = '''
                *****************************************
                ***  Please Enter A Valid Number !!!  ***
                *****************************************
            '''
            print(err_2)
            sleep(3)
            self.next_menu()
            self.install_choices()

    def install_apk(self):
        try:
            device_ip = input("Enter Your Device ip: ")
            ip_v = self.validate_ip(device_ip)
            if ip_v:
                print("")
                path = input("Enter Text Path For Your apk: ").strip()
                with open(path, "r") as f:
                    pathd = f.readlines()
                    for p in pathd:
                        p = p.strip()
                        a = p.split("\\")
                        print("")
                        print("=================================")
                        print("")
                        print(a[-1])
                        print("")
                        print("")
                        self.install_adb_command(p, device_ip)
                        sleep(5)
                        print("")
                    print("")
                    print("All applications have been successfully installed ...")
                    print(" ")
                    sleep(3)
                self.continue_or_not()
        except OSError:
            print("")
            self.message("       Enter Your A Valide Path ...")
            sleep(3)
            self.continue_or_not()

    def install_adb_command(self, path, ip):
        in_apk = fr"adb -s {ip}:{self.port} install -r {path}"
        # return in_apk
        try:
            cmd = sp.run(in_apk,
                         shell=True,
                         stdout=sp.PIPE, stderr=sp.STDOUT)
            out = cmd.stdout.decode("utf-8")
            print(out)
            if out.startswith("Performing Streamed Install\n adb.exe: filename doesn't end apk"):
                raise Exception()

        except:
            print("")
            self.message("adb.exe: filename doesn't end apk")
            print("")

    def lang_fire_cmd(self):
        device_ip = input("Enter Your Device ip: ")
        print(" ")
        ip_v = self.validate_ip(device_ip)
        if ip_v:
            lang_code = [f"adb -s {device_ip}:{self.port} shell ime enable com.aktuna.tv.keyboard/com.aktuna.leanback.ime.LeanbackImeService",
                         f"adb -s {device_ip}:{self.port} shell ime set com.aktuna.tv.keyboard/com.aktuna.leanback.ime.LeanbackImeService"]
            try:
                for lang in lang_code:
                    cmd = sp.run(lang,
                                 shell=True,
                                 stdout=sp.PIPE, stderr=sp.STDOUT)
                    out = cmd.stdout.decode("utf-8")
                    # print(cmd)
                    if out.startswith("Error: Unknown"):
                        raise Exception("")
                    else:
                        print(out)
                        sleep(3)
                self.next_menu()
            except:
                self.message("Error ...!")
                sleep(3)
                self.next_menu()

    def nested_choice(self):
        user_choice = input("Enter Your Choice: ")
        try:
            uc = int(user_choice)
            if uc == 1:
                print("")
                # print("1")
                self.install_apk()

            elif uc == 2:
                print("")
                self.install_one_apk()
                sleep(2)

            elif uc == 3:
                print("")
                self.next_menu()
                sleep(2)

            elif uc == 4:
                print("")
                self.main_menu()
                sleep(2)

            elif uc == 5:
                print("")
                exit()

            else:
                err_1 = '''
                ********************************************
                *** Plz Choose Number [ 1, 2, 3, 4 or 5] ***
                ********************************************
                '''
                print(err_1)
                sleep(3)
                self.next_menu()

        except ValueError:
            err_2 = '''
                *****************************************
                ***  Please Enter A Valid Number !!!  ***
                *****************************************
            '''
            print(err_2)
            sleep(3)
            self.next_menu()

    def nested_menu(self):
        os.system("cls")
        os.system(
            'title Setup ADB Tools [ V 1.0.0 ] - one or many apk install')
        n_m = '''
        = #################################################### =
        = ####          Choose from two options           #### =
        = #################################################### =
        = ####   [1] install from paths in text           #### =
        = ####   [2] install from apk path                #### =
        = ####   [3] return to install options menu       #### =
        = ####   [4] return to main menu                  #### =
        = ####   [5] exit from tool                       #### =
        = #################################################### =
        '''
        print(n_m)
        print(" ")
        self.nested_choice()

    def install_one_apk(self):
        # try:
        device_ip = input("Enter Your Device ip: ").strip()
        ip_v = self.validate_ip(device_ip)
        try:
            if ip_v:
                # try:
                print("")
                # try:
                path = input("Enter Path For Your apk: ").strip()
                if not path:
                    # except OSError:
                    print("")
                    self.message("       Enter Your A Valide Path ...")
                    sleep(2)
                    self.next_menu()
                else:
                    one_apk = fr"adb -s {device_ip}:{self.port} install -r {path}"
                    cmd = sp.run(one_apk,
                                 shell=True,
                                 check=True,
                                 capture_output=True)
                    out = cmd.stdout.decode("utf-8")
                    print(out)
                    sleep(3)
                    print("")
                    print("")
                    self.message(
                        "The application has been installed successfully")
                    print(" ")
                    sleep(2)
                    self.continue_or_not()
        except sp.CalledProcessError as error:
            out = error.stderr.decode("utf-8")
            print(f'\n\nError : {out}')
            sleep(3)
            self.continue_or_not()
        except OSError:
            print("")
            self.message("       Enter Your A Valide Path ...")
            sleep(2)
            self.next_menu()

    def continue_or_not(self):
        while True:
            try:
                input_str = input("Do you want continue (Y/N): ").upper()
                print("")
                if input_str == "Y":
                    print("")
                    self.next_menu()
                    break
                elif input_str == "N":
                    print("")
                    self.message("The tool will be finished")
                    sleep(3)
                    exit()
                else:
                    print("")
                    self.message("Please Choose Number [ Y ] or [ N ]")
            except ValueError:
                print("")
                self.message("Please enter a valid option !!!")


cw = ConnectWifi()


# input("                 press any key to exit ....")


'''
            *******************************************
            *** Please Choose Number [ 1 ] or [ 2 ] ***
            *******************************************
'''

'''
        ****************************************************
            {msg}          
        ****************************************************

'''

'''
        = #################################################### =
        = ####          Choose the order you need         #### =
        = #################################################### =
        = ####   [1] Mi-Box adb install backages          #### =
        = ####   [2] Mi-Stick adb install backages        #### =
        = ####   [3] Fire-Stick adb install backages      #### =
        = ####   [4] Exit  - to exit from Tool            #### =
        = #################################################### =
'''
