import banner
import os

b4nn3r = 4
c0l0r = 1

def ch4ng3b4nn3r():
    b4nn3r = int(input("select banner: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n"))
    return b4nn3r

def ch4ng3c0l0r():
    c0l0r = int(input("select color: 1(white)\n"))
    return c0l0r
    
def w1nd0w():
    banner.banner2()
    b4nn3r = ch4ng3b4nn3r()
    c0l0r = ch4ng3c0l0r()
    w = open(f"s3tt1ngs.txt", "w")
    w.write(f"b4nn3r:{b4nn3r}\nc0l0r:{c0l0r}")
    w.close()

def g3ts3tt1ng(r00td1r):
    settinglist = []
    r = open(f"{r00td1r}\\s3tt1ngs.txt", "r")
    for setting in r.read().split():
        setting = setting.split(":")
        settinglist.append(setting[1])
    return settinglist

def op3n():
    os.startfile(f"settingswindow.py")
