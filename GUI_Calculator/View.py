import tkinter
from tkinter import *
from tkinter import ttk
import Controller

GUI = Tk();
GUI.title('Calculator');
GUI.geometry('450x380');

def main_Calculator():
    GUI.mainloop();
    
input_Calculator = tkinter.Entry(GUI, width=30, font=25);
input_Calculator.grid(columnspan=3, ipadx=5, padx=10, pady=10);

btn_clear = tkinter.Button(GUI,text='C', font=8, background="white", width=4, command=Controller.Click_Clear);
btn_clear.grid(column=3, row=0, padx=10, pady=10);

btn_Num9 = tkinter.Button(GUI,text='9', font=5, background="white", width=4, command=Controller.EnventClick_Number9);
btn_Num9.grid(column=0, row=1, padx=10, pady=10);

btn_Num8 = tkinter.Button(GUI,text='8', font=5, background="white", width=4, command=Controller.EnventClick_Number8);
btn_Num8.grid(column=1, row=1, padx=10, pady=10);

btn_Num7 = tkinter.Button(GUI,text='7', font=5, background="white", width=4, command=Controller.EnventClick_Number7)
btn_Num7.grid(column=2, row=1, padx=10, pady=10);

btn_Plus = tkinter.Button(GUI,text='+', font=5, background="white", width=4, command=Controller.EnventClick_Plus);
btn_Plus.grid(column=3, row=1, padx=10, pady=10);

btn_Num6 = tkinter.Button(GUI,text='6', font=5, background="white", width=4, command=Controller.EnventClick_Number6);
btn_Num6.grid(column=0, row=2, padx=10, pady=10);

btn_Num5 = tkinter.Button(GUI,text='5', font=5, background="white", width=4, command=Controller.EnventClick_Number5);
btn_Num5.grid(column=1, row=2, padx=10, pady=10);

btn_Num4 = tkinter.Button(GUI,text='4', font=5, background="white", width=4, command=Controller.EnventClick_Number4);
btn_Num4.grid(column=2, row=2, padx=10, pady=10);

btn_Minus = tkinter.Button(GUI,text='-', font=5, background="white", width=4, command=Controller.EnventClick_Minus);
btn_Minus.grid(column=3, row=2, padx=10, pady=10);

btn_Num3 = tkinter.Button(GUI,text='3', font=5, background="white", width=4, command=Controller.EnventClick_Number3);
btn_Num3.grid(column=0, row=3, padx=10, pady=10);

btn_Num2 = tkinter.Button(GUI,text='2', font=5, background="white", width=4, command=Controller.EnventClick_Number2);
btn_Num2.grid(column=1, row=3, padx=10, pady=10);

btn_Num1 = tkinter.Button(GUI,text='1', font=5, background="white", width=4, command=Controller.EnventClick_Number1);
btn_Num1.grid(column=2, row=3, padx=10, pady=10);

btn_Multiply = tkinter.Button(GUI,text='*', font=5, background="white", width=4, command=Controller.EnventClick_Multiply);
btn_Multiply.grid(column=3, row=3, padx=10, pady=10);

btn_Num0 = tkinter.Button(GUI,text='0', font=5, background="white", width=4, command=Controller.EnventClick_Num0);
btn_Num0.grid(column=0, row=4, padx=10, pady=10);

btn_Num00 = tkinter.Button(GUI,text='00', font=5, background="white", width=4, command=Controller.EnventClick_Num00);
btn_Num00.grid(column=1, row=4, padx=10, pady=10);

btn_NumDot = tkinter.Button(GUI,text='.', font=5, background="white", width=4, command=Controller.EnventClick_Dot);
btn_NumDot.grid(column=2, row=4, padx=10, pady=10);

btn_Division = tkinter.Button(GUI,text='/', font=5, background="white", width=4, command=Controller.EnventClick_Division);
btn_Division.grid(column=3, row=4, padx=10, pady=10);

btn_Result = tkinter.Button(GUI,text='Result', font=5, background="white", width=30, command=Controller.EnventClick_Result);
btn_Result.grid(columnspan=3, ipadx=4, padx=10, pady=10);

btn_NumMod = tkinter.Button(GUI,text='%', font=5, background="white", width=5, command=Controller.EnventClick_Mod);
btn_NumMod.grid(column=3, row=5, padx=10, pady=10);