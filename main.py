import banner
import settings
import os
import subprocess
import socket

class Commandlineinterpreter:
    def __init__(self) -> None:
        self.inpu7 = ""
        self.us3rn4m3 = ""
        self.p455w0rd = ""
        self.c0mm4nd = ""
        self.l0g1ncr3d3nt14l5 = []
        self.att3mpt3dl0g1n = ""
        self.c0mm4ndl1st = ["cls", "clear", "logout", "reload", "cd", "cwd", "dir", "ls", "settings", "setting"]
        self.s3tt1ngsl1st = settings.g3ts3tt1ng()
        print(self.s3tt1ngsl1st)

    def gr4ph1cbl17(self) -> None:
        self.s3tt1ngsl1st = settings.g3ts3tt1ng()
        if self.s3tt1ngsl1st[0] == '1':
            banner.banner1()
        if self.s3tt1ngsl1st[0] == '2':
            banner.banner2()
        if self.s3tt1ngsl1st[0] == '3':
            banner.banner3()
        if self.s3tt1ngsl1st[0] == '4':
            banner.banner4()
        if self.s3tt1ngsl1st[0] == '5':
            banner.banner5()
        if self.s3tt1ngsl1st[0] == '6':
            banner.banner6()
        if self.s3tt1ngsl1st[0] == '7':
            banner.banner7()
        if self.s3tt1ngsl1st[0] == '8':
            banner.banner8()
        if self.s3tt1ngsl1st[0] == '9':
            banner.banner9()
        if self.s3tt1ngsl1st[0] == '10':
            banner.banner10()
        if self.s3tt1ngsl1st[0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            banner.banner3()

    def l0g1n(self) -> bool:
        self.us3rn4m3 = str(input("username: "))
        self.p455w0rd = str(input("password: "))
        f = open("cr3d3nt14l5.txt")
        for cr3d3nt14l in f.read().split():
            self.l0g1ncr3d3nt14l5.append(cr3d3nt14l)
        self.att3mpt3dl0g1n = self.us3rn4m3 + ":" + self.p455w0rd
        if self.att3mpt3dl0g1n in self.l0g1ncr3d3nt14l5:
            self.acc3pt3d = True
        else:
            self.acc3pt3d = False
        return self.acc3pt3d

    def g37cmd(self) -> str:
        self.c0mm4nd = str(input(f"{self.us3rn4m3}@devsec [{os.getcwd()}]> "))
        return self.c0mm4nd
    
    def cl34rscr33n(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        self.s3tt1ngsl1st = settings.g3ts3tt1ng()
        self.s3tt1ngsl1st = settings.g3ts3tt1ng()
        if self.s3tt1ngsl1st[0] == '1':
            banner.banner1()
        if self.s3tt1ngsl1st[0] == '2':
            banner.banner2()
        if self.s3tt1ngsl1st[0] == '3':
            banner.banner3()
        if self.s3tt1ngsl1st[0] == '4':
            banner.banner4()
        if self.s3tt1ngsl1st[0] == '5':
            banner.banner5()
        if self.s3tt1ngsl1st[0] == '6':
            banner.banner6()
        if self.s3tt1ngsl1st[0] == '7':
            banner.banner7()
        if self.s3tt1ngsl1st[0] == '8':
            banner.banner8()
        if self.s3tt1ngsl1st[0] == '9':
            banner.banner9()
        if self.s3tt1ngsl1st[0] == '10':
            banner.banner10()
        if self.s3tt1ngsl1st[0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            banner.banner3()
        
    def w3lc0m3m3554g3(self) -> None:   
        print(f"\nwelcome {self.us3rn4m3}\n ")

    def ch4ng3d1r(self, cmd) -> None:
        c0mm4nd1npu7 = cmd.split(" ", 1)
        try:
            if ':' in c0mm4nd1npu7[1]:
                os.chdir(c0mm4nd1npu7[1])
            else:
                os.chdir(os.getcwd() + '\\' + c0mm4nd1npu7[1])
        except:
            print(f'Error: No Such Direcotry:\n{os.getcwd()}\\{c0mm4nd1npu7[1]}\n')
    
    def d1rl1s7(self):
        listdir = os.listdir()
        for i in listdir:
            print("\t"+i)

devsec = Commandlineinterpreter()
devsec.gr4ph1cbl17()
acc3pt3d = devsec.l0g1n()
if acc3pt3d == True:
    devsec.cl34rscr33n()
    devsec.w3lc0m3m3554g3()
    if devsec.us3rn4m3 == "root":
        devsec.ch4ng3d1r("cd C:\\Users")
    else:
        devsec.ch4ng3d1r(f"cd C:\\Users\\{os.getlogin()}")
while acc3pt3d == True:
    cmd = devsec.g37cmd()
    c0mm4nd1npu7 = cmd.split(" ")
    if c0mm4nd1npu7[0] in ["cls", "clear"]:
        devsec.cl34rscr33n()
        devsec.w3lc0m3m3554g3()
    if c0mm4nd1npu7[0] in ["logout"]:
        acc3pt3d = False
    if c0mm4nd1npu7[0] in ["reload"]:
        os.chdir("C:\\Users\\Milo\\Proton Drive\\Flavinito\\My files\\Projects\\devsec cli")
        os.startfile("C:\\Users\\Milo\\Proton Drive\\Flavinito\\My files\\Projects\\devsec cli\\main.py")
        os.abort()
    if c0mm4nd1npu7[0] in ["cd"]:
        devsec.ch4ng3d1r(cmd)
    if c0mm4nd1npu7[0] in ["cwd"]:
        print(f"Current Working Directory: {os.getcwd()}")
    if c0mm4nd1npu7[0] in ["dir", "ls"]:
        devsec.d1rl1s7()
    if c0mm4nd1npu7[0] in ["settings", "setting"]:
        settings.op3n()
    if c0mm4nd1npu7[0] not in devsec.c0mm4ndl1st:
        try:
            result = subprocess.check_output(cmd, shell=True)
            result = result.decode("UTF-8")
            print(result)
        except Exception as e:
            print(e)
if acc3pt3d == False:
    devsec.cl34rscr33n()
    os.chdir("C:\\Users\\Milo\\Proton Drive\\Flavinito\\My files\\Projects\\devsec cli")
    os.startfile("C:\\Users\\Milo\\Proton Drive\\Flavinito\\My files\\Projects\\devsec cli\\main.py")
    os.abort()