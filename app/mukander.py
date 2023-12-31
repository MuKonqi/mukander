#!/usr/bin/env python3

# Copyright (C) 2023 MuKonqi (Muhammed Abdurrahman)

# Mukander is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Mukander is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Mukander.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os
import time
import getpass
username=getpass.getuser()

en="/home/"+username+"/.by-mukonqi/mukander/en.txt"
tr="/home/"+username+"/.by-mukonqi/mukander/tr.txt"

global gfs
gfs=0

def settings():
    if not os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/dark.txt") and not os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/light.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    if os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/dark.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    elif os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/light.txt"):
        bg="#FFFFFF"
        fg="#000000"
        button_bg="#000000"
        button_fg="#FFFFFF"
        a_button_bg="#FFFFFF"
        a_button_fg="#000000"
    def dark():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander/ ; rm light.txt ; touch dark.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Dark theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Koyu tema uygulandı.")
        swindow.destroy()
        if gfs == 0:
            window.destroy()
        os.system("python3 /usr/bin/mukander")
    def light():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander/ ; rm dark.txt ; touch light.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Light theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Açık tema uygulandı.")
        swindow.destroy()
        if gfs == 0:
            window.destroy()
        os.system("python3 /usr/bin/mukander")
    def langen():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander/ ; rm tr.txt ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        swindow.destroy()
        if gfs == 0:
            window.destroy()
        os.system("python3 /usr/bin/mukander")
    def langtr():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander/ ; rm en.txt ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        swindow.destroy()
        if gfs == 0:
            window.destroy()
        os.system("python3 /usr/bin/mukander")
    swindow=Tk()
    swindow.config(background=bg)
    swindow.resizable(0, 0)
    if os.path.isfile(en):
        swindow.title("Settings | Mukander")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 11 bold italic", text="Please select the theme you want to apply.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Dark", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3 ")
        sbutton2=Button(swindow, text="Light", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3" )
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 11 bold italic", text="You can change your language preferences below.")
        sspace3=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth ="3")
        sbutton4=Button(swindow, text="TÜrkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth= "3")
    if os.path.isfile(tr):
        swindow.title("Ayarlar | Mukander")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 11 bold italic", text="Lütfen uygulamak istediğiniz temayı seçiniz.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Koyu", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11", cursor="hand2", borderwidth="3")
        sbutton2=Button(swindow, text="Açık", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        sspace3=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3")
        sbutton4=Button(swindow, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3")
    stext1.pack()
    sspace1.pack()
    sbutton1.pack()
    sbutton2.pack()
    sspace2.pack()
    stext2.pack()
    sspace3.pack()
    sbutton3.pack()
    sbutton4.pack()
    mainloop()
    exit()
    
def first_start():
    global gfs
    gfs=1
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    def llangen():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', Mukander settings will open.")
        lwindow.destroy()
        settings()
    def llangtr():
        os.system("cd /home/"+username+"/.by-mukonqi/mukander ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda Mukander ayarları açılacak.")
        lwindow.destroy()
        settings()
    lwindow=Tk()
    lwindow.title("First Start of Mukander")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    ltext1=Label(lwindow, background=bg, foreground=fg, font="arial 11 bold italic", text="Please choose a language for Mukander.\nMukander için lütfen bir dil seçin.")
    ltext1.pack()
    lspace1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    lspace1.pack()
    lbutton1=Button(lwindow, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font="arial 11", cursor="hand2", borderwidth="3")
    lbutton1.pack()
    lbutton2=Button(lwindow, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 11", cursor="hand2", borderwidth="3")
    lbutton2.pack()
    mainloop()

if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
    os.system("cd /home/"+username+" ; mkdir .by-mukonqi")
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir mukander")
    first_start()
if not os.path.isdir("/home/"+username+"/.by-mukonqi/mukander"):
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir mukander")
    first_start()
    
bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/home/"+username+"/.by-mukonqi/mukander/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    gfs=1
    if os.path.isfile(en):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' settings will open.")
    elif os.path.isfile(tr):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, ayarlar 'OK' tuşuna bastığınızda açılacaktır.")
    settings()
    exit()

window=Tk()
window.config(background=bg)
window.resizable(0, 0)

def run():
    if cmdentry.get() == "" or cmdentry.get() == "Command" or cmdentry.get() == "Komut":
        if os.path.isfile(en):
            messagebox.showerror("Fatal error!","You didn't type a command.")
        elif os.path.isfile(tr):
            messagebox.showerror("Ölümcül hata!","Herhangi bir komut girmediniz.")
            return None
            
    def show():
        outputs=Toplevel()
        outputs.config(background=bg)
        outputs.resizable(0, 0) 
        if os.path.isfile(en):
            outputs.title("Outputs")
            scroll=Scrollbar(outputs)
            text4=Label(outputs, background=bg, foreground=fg, font="arial 11", text="\nThe output is below.\n")
            text5=Text(outputs, background=fg, foreground=bg, yscrollcommand=scroll.set)
            text5.insert(END, out)
            text5.insert(END, err)
            scroll.config(command=text5.yview)
            space5=Label(outputs, background=bg, foreground=fg, text="\n", font="arial 3")
            button2=Button(outputs, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=outputs.destroy)
        elif os.path.isfile(tr):
            outputs.title("Çıktılar")
            scroll=Scrollbar(outputs)
            text4=Label(outputs, background=bg, foreground=fg, font="arial 11", text="\nÇıktı aşağıdadır.\n")
            text5=Text(outputs, background=fg, foreground=bg, yscrollcommand=scroll.set)            
            text5.insert(END, out)
            text5.insert(END, err)
            scroll.config(command=text5.yview)
            space5=Label(outputs, background=bg, foreground=fg, text="\n", font="arial 3")
            button2=Button(outputs, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=outputs.destroy)            
        scroll.pack(side=RIGHT,fill=Y)
        text4.pack()
        text5.pack()
        text5.config(state=DISABLED)
        space5.pack()
        button2.pack()
          
    text3=Label(window, background=bg, foreground=fg, font="arial 11 bold italic")
    text3.pack() 
    tic = time.time()
    if passentry.get() == "Password (for sudo)" or passentry.get() == "Şifre (sudo için)" or passentry.get() == "":
        result = subprocess.Popen(cmdentry.get(), shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
    else:
        result = subprocess.Popen("echo "+passentry.get()+" | sudo -S "+cmdentry.get(), shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
    (out, err) = result.communicate()
    toc = time.time()
    if os.path.isfile(en):
        text3.config(text="Status: Completed in "+str(toc - tic)+" seconds.")
        button1=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Show results",command=show)
    elif os.path.isfile(tr):
        text3.config(text="Durum: "+str(toc - tic)+" saniyede tamamlandı.")
        button1=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Sonuçları göster",command=show)
    button1.pack()

def dce(e):
    cmdentry.delete(0, END)
def dpe(e):
    passentry.delete(0, END)
    
if os.path.isfile(en):
    window.title("Main Page | Mukander")
    text1=Label(window, background=bg, foreground=fg, font="arial 11 bold italic", text="You can type command below.\nJust fill in the password box whenever you want to use sudo.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    cmdentry=Entry(window)
    cmdentry.insert(0, "Command")
    cmdentry.bind("<FocusIn>", dce)
    passentry=Entry(window)
    passentry.insert(0, "Password (for sudo)")
    passentry.bind("<FocusIn>", dpe)
    space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")    
    confirm=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Run",command=run)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 5")
    sobutton=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Settings", command=settings)
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
elif os.path.isfile(tr):
    window.title("Ana Sayfa | Mukander")
    text1=Label(window, background=bg, foreground=fg, font="arial 11 bold italic", text="Aşağıda komut girebilirsiniz.\nSadece sudo kullanmak istediğiniz zamanlarda şifre kutucuğunu doldurun.")
    space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    cmdentry=Entry(window)
    cmdentry.insert(0, "Komut")
    cmdentry.bind("<FocusIn>", dce)
    passentry=Entry(window)
    passentry.insert(0, "Şifre (sudo için)")
    passentry.bind("<FocusIn>", dpe)
    space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
    confirm=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Çalıştır",command=run)
    space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 5")
    sobutton=Button(window, font="arial 11", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, background=button_bg, borderwidth="3", text="Ayarlar", command=settings)
    space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
text1.pack()
space1.pack()
cmdentry.pack()
passentry.pack()
space4.pack()
confirm.pack()
space2.pack()
sobutton.pack()
space3.pack()

mainloop()