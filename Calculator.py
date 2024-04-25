from tkinter import *

win = Tk()
win.geometry("620x600")
F = StringVar()
ANS = StringVar()

# MANG HÌNH
def SRC(f):
    F.set(f)
    screen = Entry(win, textvariable=F, bd=5, width=40, font=("Arial", 25))
    screen.grid(row = 0, column = 0, columnspan = 3, sticky="nsew")
#MANG ĐÁP ÁN
def SR_ANS(kq):
    ANS.set(kq)
    screen = Entry(win, textvariable=ANS, bd=5, width=20, font=("Arial", 25))
    screen.grid(row = 0, column = 3, columnspan = 2, sticky="nsew")
#NÚT SỐ
def BUT():
    num = 1
    for i in range (3):
        for j in range(3):
            b = Button(win, text = str(num), width=10, command = lambda x = num: IN(x), font=("Arial", 25))
            b.grid(row = i + 1, column = j, sticky="nsew")
            num += 1
    b = Button(win, text = '0', width=10, command = lambda x = 0: IN(x), font=("Arial", 25))
    b.grid(row = 4, column = 1, sticky="nsew")
# #NÚT DẤU
def BUT_SIG():
    sign = ["+", "-", "*", "/"]
    num = 0
    for i in range(2):
        for j in range(2):
            b_s = Button(win, text = sign[num], width=10, command = lambda x = sign[num]: SIG(x), font=("Arial", 25))
            b_s.grid(row = i + 1, column = j + 3, sticky="nsew")
            num += 1
#DẤU ĐB
def EQ_SIG():
    b_eq = Button(win, text = "=", width=20, font=("Arial", 25), command = EQ)
    b_eq.grid(row = 4, column = 3, columnspan=2, sticky="nsew")
    
    b_re = Button(win, text = "S", width=10, font=("Arial", 25), command = RS)
    b_re.grid(row = 3, column = 3, sticky="nsew")
    
    b_remo = Button(win, text = "<=", width=10, font=("Arial", 25), command= DL)
    b_remo.grid(row = 3, column = 4, sticky="nsew")
    
#IN SỐ
def IN(n):
    global f
    global kq
    f = f + str(n)
    kq = ''
    #print(f)
    SRC(f)
    SR_ANS(kq)
#IN DẤU
def SIG(s):
    global f
    global kq
    f = f + str(s)
    kq = ''
    #print(f)
    SRC(f)
    SR_ANS(kq)
#XÓA HẾT
def RS():
    global f
    global kq
    f = ''
    kq = ''
    SRC(f)
    SR_ANS(kq)
#XÓA 1
def DL():
    global f
    global kq
    F = ''
    for i in range(0, len(f)-1):
        F = F + f[i]
    f = F
    kq = ''
    SRC(f)
    SR_ANS(kq)
#DẤU BẰNG
def EQ():
    global kq
    kq = eval(f)
    SR_ANS(kq)
    

# MAIN
f = ''
kq = ''
SRC(f)
SR_ANS(kq)
BUT()
BUT_SIG()
EQ_SIG()
#CO DÃN
for i in range(1, 4):
    win.rowconfigure(i, weight=1)
    win.columnconfigure(i-1, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(4, weight=1)
win.columnconfigure(4, weight=1)
win.columnconfigure(3, weight=1)
win.mainloop()
