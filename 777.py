from tkinter import *
from random import *
a=100
b=1
exp=0
srt=0
intl=0
agi=0
def clear_window():
    for widget in window.winfo_children():
        if not isinstance(widget, Menu):
            widget.destroy()

def clicked():
    global a
    global b
    global exp
    global srt
    global intl
    a-=randint(b,b*2)
    lbl["text"]=a
    if a <= 0:
        b+=1
        a=b*10
        exp += 1
def edit_click():
    window.destroy()
    
def sila_click():
    global srt
    global exp
    global lbl_srt
    global lbl_exp
    srt +=1
    lbl_srt["text"] = f"сила {srt}"
    exp -=1
    lbl_exp["text"] = f"опыт {exp}"
def intellekt_click():
    global intl
    global exp
    global lbl_exp
    global lbl_intl
    intl +=1
    lbl_intl["text"] = f"интелект {intl}"
    exp -=1
    lbl_exp["text"] = f"опыт {exp}"
def lovkost_click():
    global agi
    global exp
    global lbl_exp
    global lbl_agi
    agi +=1
    lbl_agi["text"] = f"ловкость {agi}"
    exp -=1
    lbl_exp["text"] = f"опыт {exp}"




def player_click():
    global exp
    global srt
    global intl
    global agi
    global lbl_exp
    global lbl_srt
    global lbl_intl
    global lbl_agi
    #root=Tk()
    #root.title("прокачка")
    #root.geometry("2000x1000")
    clear_window()
    lbl_exp=Label(window,text=f"опыт {exp}")
    lbl_srt=Label(window,text="сила")
    lbl_intl=Label(window,text="интелект")
    lbl_agi=Label(window,text="ловкость")

    lbl_exp.grid(column=0,row=1)
    lbl_srt.grid(column=0,row=2)
    lbl_intl.grid(column=0,row=3)
    lbl_agi.grid(column=0,row=4)
    

    btn_srt=Button(window,text="+",command=sila_click)
    btn_srt.grid(column=1,row=2)
   # lbl_str["text"]=str
    btn_intl=Button(window,text="+",command=intellekt_click)
    btn_intl.grid(column=1,row=3)

    btn_agi=Button(window,text="+",command=lovkost_click)
    btn_agi.grid(column=1,row=4)


window=Tk()
window.title("кликер")
window.geometry("2000x1000")

lbl=Label(window,text="Кликер",font=("times new roman",25))
lbl.pack()

btn=Button(window,text="кликер",command=clicked, width=50,height=20)
btn.pack()

file_menu=Menu()
file_menu.add_command(label="новая")
file_menu.add_command(label="сохранить")
file_menu.add_command(label="открыть")
file_menu.add_separator()
file_menu.add_command(label="выйти",command=edit_click)

player_menu=Menu()
player_menu.add_command(label="навык",command=player_click)
player_menu.add_command(label="экиперовка",command=player_click)


main_menu=Menu()
main_menu.add_cascade(label="игрок",menu=player_menu)
main_menu.add_cascade(label="игра", menu=file_menu)
main_menu.add_cascade(label="магазин")

   

window.config(menu=main_menu)
window.mainloop()

