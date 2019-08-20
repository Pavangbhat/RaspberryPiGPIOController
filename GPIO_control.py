from tkinter import *
#GPIO pins intiallisation

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, GPIO.LOW)
GPIO.setup(9, GPIO.OUT)
GPIO.output(9, GPIO.LOW)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.LOW)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.LOW)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)

win=Tk()
win.configure(background="purple3")
win.geometry("700x800")
win.title("GPIO CONTROLLER")
fonts = ('times', 20, 'bold')

f1=Frame(bg="purple3")
f1.pack(side="top")
f2=Frame(pady=30,bg="purple3")
f2.pack(side="top")

note=Label(f2,text="Take a look on\n readme before using",bg="red",fg="white")
note.config(font=fonts)
note.grid(row=24,column=1)
head=Label(f2,text="GPIO CONTROLLER",bg="black",fg="white")
head.config(font=fonts)
head.grid(row=23,column=1)

def fun():
    if GPIO.input(2)==False:
        GPIO.output(2,True)
    else:
        GPIO.output(2,False)


def fun1():
    if GPIO.input(3)==False:
        GPIO.output(3,True)
    else:
        GPIO.output(3,False)


def fun2():
    if GPIO.input(4)==False:
        GPIO.output(4,True)
    else:
        GPIO.output(4,False)


def fun3():
    if GPIO.input(14)==False:
        GPIO.output(14,True)
    else:
        GPIO.output(14,False)


def fun4():
    if GPIO.input(15)==False:
        GPIO.output(15,True)
    else:
        GPIO.output(15,False)


def fun5():
    if GPIO.input(17)==False:
        GPIO.output(17,True)
    else:
        GPIO.output(17,False)


def fun6():
    if GPIO.input(18)==False:
        GPIO.output(18,True)
    else:
        GPIO.output(18,False)


def fun7():
    if GPIO.input(27)==False:
        GPIO.output(27,True)
    else:
        GPIO.output(27,False)


def fun8():
    if GPIO.input(22)==False:
        GPIO.output(22,True)
    else:
        GPIO.output(22,False)


def fun9():
    if GPIO.input(23)==False:
        GPIO.output(23,True)
    else:
        GPIO.output(23,False)


def fun10():
    if GPIO.input(24)==False:
        GPIO.output(24,True)
    else:
        GPIO.output(24,False)


def fun11():
    if GPIO.input(10)==False:
        GPIO.output(10,True)
    else:
        GPIO.output(10,False)


def fun12():
    if GPIO.input(9)==False:
        GPIO.output(9,True)
    else:
        GPIO.output(9,False)


def fun13():
    if GPIO.input(25)==False:
        GPIO.output(25,True)
    else:
        GPIO.output(25,False)


def fun14():
    if GPIO.input(11)==False:
        GPIO.output(11,True)
    else:
        GPIO.output(11,False)


def fun15():
    if GPIO.input(8)==False:
        GPIO.output(8,True)
    else:
        GPIO.output(8,False)


def fun16():
    if GPIO.input(7)==False:
        GPIO.output(7,True)
    else:
        GPIO.output(7,False)


def fun17():
    if GPIO.input(5)==False:
        GPIO.output(5,True)
    else:
        GPIO.output(5,False)


def fun18():
    if GPIO.input(6)==False:
        GPIO.output(6,True)
    else:
        GPIO.output(6,False)


def fun19():
    if GPIO.input(12)==False:
        GPIO.output(12,True)
    else:
        GPIO.output(12,False)


def fun20():
    if GPIO.input(13)==False:
        GPIO.output(13,True)
    else:
        GPIO.output(13,False)


def fun21():
    if GPIO.input(19)==False:
        GPIO.output(19,True)
    else:
        GPIO.output(19,False)


def fun22():
    if GPIO.input(16)==False:
        GPIO.output(16,True)
    else:
        GPIO.output(16,False)


def fun23():
    if GPIO.input(26)==False:
        GPIO.output(26,True)
    else:
        GPIO.output(26,False)


def fun24():
    if GPIO.input(20)==False:
        GPIO.output(20,True)
    else:
        GPIO.output(20,False)


def fun25():
    if GPIO.input(21)==False:
        GPIO.output(21,True)
    else:
        GPIO.output(21,False)
#exit button
def exitbutton():
    if GPIO.input(2)==True:
        GPIO.output(2,False)
    if GPIO.input(3)==True:
        GPIO.output(3,False)
    if GPIO.input(4)==True:
        GPIO.output(4,False)
    if GPIO.input(14)==True:
        GPIO.output(14,False)
    if GPIO.input(15)==True:
        GPIO.output(15,False)
    if GPIO.input(17)==True:
        GPIO.output(17,False)
    if GPIO.input(18)==True:
        GPIO.output(18,False)
    if GPIO.input(27)==True:
        GPIO.output(27,False)
    if GPIO.input(22)==True:
        GPIO.output(22,False)
    if GPIO.input(23)==True:
        GPIO.output(23,False)
    if GPIO.input(24)==True:
        GPIO.output(24,False)
    if GPIO.input(10)==True:
        GPIO.output(10,False)
    if GPIO.input(9)==True:
        GPIO.output(9,False)
    if GPIO.input(25)==True:
        GPIO.output(25,False)
    if GPIO.input(11)==True:
        GPIO.output(11,False)
    if GPIO.input(8)==True:
        GPIO.output(8,False)
    if GPIO.input(7)==True:
        GPIO.output(7,False)
    if GPIO.input(5)==True:
        GPIO.output(5,False)
    if GPIO.input(6)==True:
        GPIO.output(6,False)
    if GPIO.input(12)==True:
        GPIO.output(12,False)
    if GPIO.input(13)==True:
        GPIO.output(13,False)
    if GPIO.input(19)==True:
        GPIO.output(19,False)
    if GPIO.input(16)==True:
        GPIO.output(16,False)
    if GPIO.input(26)==True:
        GPIO.output(26,False)
    if GPIO.input(20)==True:
        GPIO.output(20,False)
    if GPIO.input(21)==True:
        GPIO.output(21,False)
    win.quit()
#labels

l1=Label(f1,text="3*3",bg="red")
l1.config(font=fonts)
l2=Label(f1,text="5v",bg="red")
l2.config(font=fonts)
l3=Label(f1,text="GPIO 2",bg="turquoise1")
l3.config(font=fonts)
l4=Label(f1,text="5v",bg="red")
l4.config(font=fonts)
l5=Label(f1,text="GPIO 3",bg="turquoise1")
l5.config(font=fonts)
l6=Label(f1,text="ground",bg="black",fg="white")
l6.config(font=fonts)
l7=Label(f1,text="GPIO 4",bg="turquoise1")
l7.config(font=fonts)
l8=Label(f1,text="GPIO 14",bg="turquoise1")
l8.config(font=fonts)
l9=Label(f1,text="ground",bg="black",fg="white")
l9.config(font=fonts)
l10=Label(f1,text="GPIO 15",bg="turquoise1")
l10.config(font=fonts)
l11=Label(f1,text="GPIO 17",bg="turquoise1")
l11.config(font=fonts)
l12=Label(f1,text="GPIO 18",bg="turquoise1")
l12.config(font=fonts)
l13=Label(f1,text="GPIO 27",bg="turquoise1")
l13.config(font=fonts)
l14=Label(f1,text="ground",bg="black",fg="white")
l14.config(font=fonts)
l15=Label(f1,text="GPIO 22",bg="turquoise1")
l15.config(font=fonts)
l16=Label(f1,text="GPIO 23",bg="turquoise1")
l16.config(font=fonts)
l17=Label(f1,text="3v3",bg="red")
l17.config(font=fonts)
l18=Label(f1,text="GPIO 24",bg="turquoise1")
l18.config(font=fonts)
l19=Label(f1,text="GPIO 10",bg="turquoise1")
l19.config(font=fonts)
l20=Label(f1,text="ground",bg="black",fg="white")
l20.config(font=fonts)
l21=Label(f1,text="GPIO 9",bg="turquoise1")
l21.config(font=fonts)
l22=Label(f1,text="GPIO 25",bg="turquoise1")
l22.config(font=fonts)
l23=Label(f1,text="GPIO 11",bg="turquoise1")
l23.config(font=fonts)
l24=Label(f1,text="GPIO 8",bg="turquoise1")
l24.config(font=fonts)
l25=Label(f1,text="ground",bg="black",fg="white")
l25.config(font=fonts)
l26=Label(f1,text="GPIO 7",bg="turquoise1")
l26.config(font=fonts)
l27=Label(f1,text="ID_SD",bg="yellow")
l27.config(font=fonts)
l28=Label(f1,text="ID_SC",bg="yellow")
l28.config(font=fonts)
l29=Label(f1,text="GPIO 5",bg="turquoise1")
l29.config(font=fonts)
l30=Label(f1,text="ground",bg="black",fg="white")
l30.config(font=fonts)
l31=Label(f1,text="GPIO 6",bg="turquoise1")
l31.config(font=fonts)
l32=Label(f1,text="GPIO 12",bg="turquoise1")
l32.config(font=fonts)
l33=Label(f1,text="GPIO 13",bg="turquoise1")
l33.config(font=fonts)
l34=Label(f1,text="ground",bg="black",fg="white")
l34.config(font=fonts)
l35=Label(f1,text="GPIO 19",bg="turquoise1")
l35.config(font=fonts)
l36=Label(f1,text="GPIO 16",bg="turquoise1")
l36.config(font=fonts)
l37=Label(f1,text="GPIO 26",bg="turquoise1")
l37.config(font=fonts)
l38=Label(f1,text="GPIO 20",bg="turquoise1")
l38.config(font=fonts)
l39=Label(f1,text="ground",bg="black",fg="white")
l39.config(font=fonts)
l40=Label(f1,text="GPIO 21",bg="turquoise1")
l40.config(font=fonts)
#check buttons

c1=Checkbutton(f1,bg="purple3")
c2=Checkbutton(f1,bg="purple3")
c3=Checkbutton(f1,command=fun,bg="purple3")
c4=Checkbutton(f1,bg="purple3")
c5=Checkbutton(f1,command=fun1,bg="purple3")
c6=Checkbutton(f1,bg="purple3")
c7=Checkbutton(f1,command=fun2,bg="purple3")
c8=Checkbutton(f1,command=fun3,bg="purple3")
c9=Checkbutton(f1,bg="purple3")
c10=Checkbutton(f1,command=fun4,bg="purple3")
c11=Checkbutton(f1,command=fun5,bg="purple3")
c12=Checkbutton(f1,command=fun6,bg="purple3")
c13=Checkbutton(f1,command=fun7,bg="purple3")
c14=Checkbutton(f1,bg="purple3")
c15=Checkbutton(f1,command=fun8,bg="purple3")
c16=Checkbutton(f1,command=fun9,bg="purple3")
c17=Checkbutton(f1,bg="purple3")
c18=Checkbutton(f1,command=fun10,bg="purple3")
c19=Checkbutton(f1,command=fun11,bg="purple3")
c20=Checkbutton(f1,bg="purple3")
c21=Checkbutton(f1,command=fun12,bg="purple3")
c22=Checkbutton(f1,command=fun13,bg="purple3")
c23=Checkbutton(f1,command=fun14,bg="purple3")
c24=Checkbutton(f1,command=fun15,bg="purple3")
c25=Checkbutton(f1,bg="purple3")
c26=Checkbutton(f1,command=fun16,bg="purple3")
c27=Checkbutton(f1,bg="purple3")
c28=Checkbutton(f1,bg="purple3")
c29=Checkbutton(f1,command=fun17,bg="purple3")
c30=Checkbutton(f1,bg="purple3")
c31=Checkbutton(f1,command=fun18,bg="purple3")
c32=Checkbutton(f1,command=fun19,bg="purple3")
c33=Checkbutton(f1,command=fun20,bg="purple3")
c34=Checkbutton(f1,bg="purple3")
c35=Checkbutton(f1,command=fun21,bg="purple3")
c36=Checkbutton(f1,command=fun22,bg="purple3")
c37=Checkbutton(f1,command=fun23,bg="purple3")
c38=Checkbutton(f1,command=fun24,bg="purple3")
c39=Checkbutton(f1,bg="purple3")
c40=Checkbutton(f1,command=fun25,bg="purple3")

#label arrangements

l1.grid(row=1,stick=E)
l2.grid(row=1,column=2,stick=E)
l3.grid(row=2,column=0,stick=E)
l4.grid(row=2,column=2,stick=E)
l5.grid(row=3,column=0,stick=E)
l6.grid(row=3,column=2,stick=E)
l7.grid(row=4,column=0,stick=E)
l8.grid(row=4,column=2,stick=E)
l9.grid(row=5,column=0,stick=E)
l10.grid(row=5,column=2,stick=E)
l11.grid(row=6,column=0,stick=E)
l12.grid(row=6,column=2,stick=E)
l13.grid(row=7,column=0,stick=E)
l14.grid(row=7,column=2,stick=E)
l15.grid(row=8,column=0,stick=E)
l16.grid(row=8,column=2,stick=E)
l17.grid(row=9,column=0,stick=E)
l18.grid(row=9,column=2,stick=E)
l19.grid(row=10,column=0,stick=E)
l20.grid(row=10,column=2,stick=E)
l21.grid(row=11,column=0,stick=E)
l22.grid(row=11,column=2,stick=E)
l23.grid(row=12,column=0,stick=E)
l24.grid(row=12,column=2,stick=E)
l25.grid(row=13,column=0,stick=E)
l26.grid(row=13,column=2,stick=E)
l27.grid(row=14,column=0,stick=E)
l28.grid(row=14,column=2,stick=E)
l29.grid(row=15,column=0,stick=E)
l30.grid(row=15,column=2,stick=E)
l31.grid(row=16,column=0,stick=E)
l32.grid(row=16,column=2,stick=E)
l33.grid(row=17,column=0,stick=E)
l34.grid(row=17,column=2,stick=E)
l35.grid(row=18,column=0,stick=E)
l36.grid(row=18,column=2,stick=E)
l37.grid(row=19,column=0,stick=E)
l38.grid(row=19,column=2,stick=E)
l39.grid(row=20,column=0,stick=E)
l40.grid(row=20,column=2,stick=E)

#check button arrangement

c1.grid(row=1,column=1)
c2.grid(row=1,column=4)
c3.grid(row=2,column=1)
c4.grid(row=2,column=4)
c5.grid(row=3,column=1)
c6.grid(row=3,column=4)
c7.grid(row=4,column=1)
c8.grid(row=4,column=4)
c9.grid(row=5,column=1)
c10.grid(row=5,column=4)
c11.grid(row=6,column=1)
c12.grid(row=6,column=4)
c13.grid(row=7,column=1)
c14.grid(row=7,column=4)
c15.grid(row=8,column=1)
c16.grid(row=8,column=4)
c17.grid(row=9,column=1)
c18.grid(row=9,column=4)
c19.grid(row=10,column=1)
c20.grid(row=10,column=4)
c21.grid(row=11,column=1)
c22.grid(row=11,column=4)
c23.grid(row=12,column=1)
c24.grid(row=12,column=4)
c25.grid(row=13,column=1)
c26.grid(row=13,column=4)
c27.grid(row=14,column=1)
c28.grid(row=14,column=4)
c29.grid(row=15,column=1)
c30.grid(row=15,column=4)
c31.grid(row=16,column=1)
c32.grid(row=16,column=4)
c33.grid(row=17,column=1)
c34.grid(row=17,column=4)
c35.grid(row=18,column=1)
c36.grid(row=18,column=4)
c37.grid(row=19,column=1)
c38.grid(row=19,column=4)
c39.grid(row=20,column=1)
c40.grid(row=20, column=4)

b1=Button(f2,text="EXIT",bg="snow3",command=exitbutton,width=5,height=1)
#b1.config(fonts=font)
b1.grid(row=22,column=1)

win.mainloop()
