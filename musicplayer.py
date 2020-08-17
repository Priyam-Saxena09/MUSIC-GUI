from tkinter import *
from PIL import Image, ImageTk
from functools import partial
from pygame import mixer
from win32com.client import Dispatch
import tkinter.messagebox as ms
music = Tk()
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def play(song):
    mixer.init()
    mixer.music.stop()
    speak("Now Enjoy the Song " + song)
    mixer.music.load("Music/" + song + ".mp3")
    mixer.music.play()
    img = Image.open("Images/"+ song + ".jpg").resize((1600, 340), Image.ANTIALIAS)
    filename = ImageTk.PhotoImage(img)
    canvas.image = filename
    canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.pack()
def exit():
    opt = ms.askquestion("Exit","Do you Want to exit the Music Player?")
    if(opt == "yes"):
        music.destroy()
    else:
        pass    
music.geometry("1330x1000")
music.title("Music Player")
music.maxsize(2500,2500)
music.wm_iconbitmap("Images/Bokehlicia-Captiva-Multimedia-audio-player.ico")
ti = Label(text="Music Player",fg="gold",bg="black",font="Times 23 bold")
ti.pack(fill="both",side=TOP)
f1 = Frame(pady=8,padx=250,bg="black")
f1.pack()
Button(f1,text="Aankh Marey",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Aankh Marey")).grid(row=0,column=0,padx=10)
Button(f1,text="Apna Time Aayega",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Apna Time Aayega")).grid(row=0,column=2,padx=10)
Button(f1,text="Aukaat",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Aukaat")).grid(row=0,column=4,padx=10)
Button(f1,text="Baby Ko Bass Pasand Hai",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Baby Ko Bass Pasand Hai")).grid(row=0,column=6,padx=10)
Button(f1,text="Ban Ja Rani",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Ban Ja Rani")).grid(row=0,column=8,padx=10)
Button(f1,text="Bezubaan Kab Se",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Bezubaan Kab Se")).grid(row=1,column=0,padx=10,pady=8)
Button(f1,text="Chale Aana",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Chale Aana")).grid(row=1,column=2,padx=10,pady=8)
Button(f1,text="Chandigarh Mein",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Chandigarh Mein")).grid(row=1,column=4,padx=10,pady=8)
Button(f1,text="Coca Cola",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Coca Cola")).grid(row=1,column=6,padx=10,pady=8)
Button(f1,text="Daru Badnaam",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Daru Badnaam")).grid(row=1,column=8,padx=10,pady=8)
Button(f1,text="Dheeme Dheeme",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Dheeme Dheeme")).grid(row=2,column=0,padx=10,pady=8)
Button(f1,text="Dil Cheez Tujhe Dedi",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Dil Cheez Tujhe Dedi")).grid(row=2,column=2,padx=10,pady=8)
Button(f1,text="Dil Diyan Gallan",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Dil Diyan Gallan")).grid(row=2,column=4,padx=10,pady=8)
Button(f1,text="Enni Soni",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Enni Soni")).grid(row=2,column=6,padx=10,pady=8)
Button(f1,text="Galti Se Mistake",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Galti Se Mistake")).grid(row=2,column=8,padx=10,pady=8)
Button(f1,text="Get Ready To Fight Reloaded",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Get Ready To Fight Reloaded")).grid(row=3,column=0,padx=10,pady=8)
Button(f1,text="Ghungroo",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Ghungroo")).grid(row=3,column=2,padx=10,pady=8)
Button(f1,text="Haan Main Galat",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Haan Main Galat")).grid(row=3,column=4,padx=10,pady=8)
Button(f1,text="Hauli Hauli",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Hauli Hauli")).grid(row=3,column=6,padx=10,pady=8)
Button(f1,text="High Heels",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"High Heels")).grid(row=3,column=8,padx=10,pady=8)
Button(f1,text="Ikk Kudi",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Ikk Kudi")).grid(row=4,column=0,padx=10,pady=8)
Button(f1,text="Illegal Weapon 2.0",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Illegal Weapon 2.0")).grid(row=4,column=2,padx=10,pady=8)
Button(f1,text="Jab Tak",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Jab Tak")).grid(row=4,column=4,padx=10,pady=8)
Button(f1,text="Jag Ghoomeya",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Jag Ghoomeya")).grid(row=4,column=6,padx=10,pady=8)
Button(f1,text="Jai Jai Shivshankar",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Jai Jai Shivshankar")).grid(row=4,column=8,padx=10,pady=8)
Button(f1,text="Kaun Tujhe",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Kaun Tujhe")).grid(row=5,column=0,padx=10,pady=8)
Button(f1,text="Lagdi Lahore Di",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Lagdi Lahore Di")).grid(row=5,column=2,padx=10,pady=8)
Button(f1,text="Main Hoon Hero Tera",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Main Hoon Hero Tera")).grid(row=5,column=4,padx=10,pady=8)
Button(f1,text="Main Tera Boyfriend",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Main Tera Boyfriend")).grid(row=5,column=6,padx=10,pady=8)
Button(f1,text="Mere Rashke Qamar",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Mere Rashke Qamar")).grid(row=5,column=8,padx=10,pady=8)
Button(f1,text="Munna Badnaam Hua",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Munna Badnaam Hua")).grid(row=6,column=0,padx=10,pady=8)
Button(f1,text="Muqabla",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Muqabla")).grid(row=6,column=2,padx=10,pady=8)
Button(f1,text="Nachange Saari Raat",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Nachange Saari Raat")).grid(row=6,column=4,padx=10,pady=8)
Button(f1,text="Nachde Ne Saare",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Nachde Ne Saare")).grid(row=6,column=6,padx=10,pady=8)
Button(f1,text="Nit Khair Manga",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Nit Khair Manga")).grid(row=6,column=8,padx=10,pady=8)
Button(f1,text="O Saathi",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"O Saathi")).grid(row=7,column=0,padx=10,pady=8)
Button(f1,text="Oh Ho Ho Ho",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Oh Ho Ho Ho")).grid(row=7,column=2,padx=10,pady=8)
Button(f1,text="Oye Oye",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Oye Oye")).grid(row=7,column=4,padx=10,pady=8)
Button(f1,text="Patola",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Patola")).grid(row=7,column=6,padx=10,pady=8)
Button(f1,text="Phir Kabhi",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Phir Kabhi")).grid(row=7,column=8,padx=10,pady=8)
Button(f1,text="Rayzr Mera Swag",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Rayzr Mera Swag")).grid(row=8,column=0,padx=10,pady=8)
Button(f1,text="Sauda Khara Khara",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Sauda Khara Khara")).grid(row=8,column=2,padx=10,pady=8)
Button(f1,text="Shaitan Ka Saala",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Shaitan Ka Saala")).grid(row=8,column=4,padx=10,pady=8)
Button(f1,text="Shankara Re Shankara",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Shankara Re Shankara")).grid(row=8,column=6,padx=10,pady=8)
Button(f1,text="Suit Suit",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Suit Suit")).grid(row=8,column=8,padx=10,pady=8)
Button(f1,text="Swag Se Swagat",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Swag Se Swagat")).grid(row=9,column=0,padx=10,pady=8)
Button(f1,text="Tera Baap Aaya",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Tera Baap Aaya")).grid(row=9,column=2,padx=10,pady=8)
Button(f1,text="Teri Mere Kahaani",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Teri Mere Kahaani")).grid(row=9,column=4,padx=10,pady=8)
Button(f1,text="The Hook Up Song",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"The Hook Up Song")).grid(row=9,column=6,padx=10,pady=8)
Button(f1,text="Yaad Piya Ki Aane Lagi",font="Helvetica 13 bold",relief=SUNKEN,command=partial(play,"Yaad Piya Ki Aane Lagi")).grid(row=9,column=8,padx=10,pady=8)
canvas = Canvas(height=1000,width=1900,bg="black")
men = Menu()
men.add_command(label="Exit",command=exit)
music.config(menu=men)
canvas.pack()
music.mainloop()