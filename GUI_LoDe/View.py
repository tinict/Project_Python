from tkinter import scrolledtext
import tkinter
from tkinter import *
from tkinter import ttk
import Controller

GUI = Tk();
GUI.title('Trò Chơi Lô Đề');
GUI.geometry('1200x700');

def main_TroChoiLoDe():
    GUI.mainloop();

val1 = tkinter.IntVar();
val2 = tkinter.IntVar();
val3 = tkinter.IntVar();
val4 = tkinter.IntVar();
val5 = tkinter.IntVar();

tkinter.Label(text='Trò Chơi Lô Đề', font=14).grid(column=2, row=0, padx=10, pady=10);

tkinter.Label(text='I. Chơi Lô').grid(column=0, row=1, padx=10, pady=10);
tkinter.Label(text='Chọn số: ').grid(column=0, row=2, padx=10, pady=10);

ip_1 = tkinter.Entry(width=24, textvariable=val1);
ip_1.grid(column=1, row=2, padx=10, pady=10);

tkinter.Label(text='Đánh mấy điểm: ').grid(column=3, row=2, padx=10, pady=10);

ip_2 = tkinter.Entry(width=24, textvariable=val2);
ip_2.grid(column=4, row=2, padx=10, pady=10);

btn_1 = tkinter.Button(text='Chơi đi đừng sợ', bg='white', command=Controller.ResultXoSoLo);
btn_1.grid(column=3, row=3, padx=10, pady=10);
tkinter.Label(text='1 điểm = 23.000 VNĐ ').grid(column=4, row=3, padx=10, pady=10);

tkinter.Label(text='II. Chơi Đề').grid(column=0, row=3, padx=10, pady=10);
tkinter.Label(text='Chọn số: ').grid(column=0, row=4, padx=10, pady=10);

ip_3 = tkinter.Entry(width=24, textvariable=val3);
ip_3.grid(column=1, row=4, padx=10, pady=10);

tkinter.Label(text='Đánh mấy điểm: ').grid(column=3, row=4, padx=10, pady=10);

ip_4 = tkinter.Entry(width=24, textvariable=val4);
ip_4.grid(column=4, row=4, padx=10, pady=10);

btn_2 = tkinter.Button(text='Chơi đi đừng sợ', bg='white', command=Controller.ResultXoSoDe);
btn_2.grid(column=3, row=5, padx=10, pady=10);
tkinter.Label(text='1 điểm = 1.000 VNĐ ').grid(column=4, row=5, padx=10, pady=10);

boxTextArea = scrolledtext.ScrolledText(GUI, wrap = tkinter.WORD, width = 60, height = 20);
boxTextArea.grid(column=2, row=7, padx=10, pady=10);
boxTextArea.config(state=DISABLED);

tkinter.Label(text='Tổng tiền: 1.000.000 VND ').grid(column=0, row=9, padx=10, pady=10);
tkinter.Label(text='Số tiền còn lại: ').grid(column=0, row=10, padx=10, pady=10);
ip_5 = tkinter.Entry(width=24, textvariable=val5);
ip_5.grid(column=1, row=10, padx=10, pady=10);
ip_5.insert(INSERT, '1000000');
