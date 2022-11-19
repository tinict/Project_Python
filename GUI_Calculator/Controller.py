import View
from tkinter import *
from math import *

def Click_Clear():
    View.input_Calculator.delete(0,END);
    
def EnventClick_Number9():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num9.cget('text'));
    print(View.btn_Num9.cget('text'));

def EnventClick_Number8():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num8.cget('text'));
    print(View.btn_Num8.cget('text'));
    
def EnventClick_Number7():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num7.cget('text'));
    print(View.btn_Num7.cget('text'));

def EnventClick_Plus():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Plus.cget('text'));
    print(View.btn_Plus.cget('text'));
    
def EnventClick_Number6():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num6.cget('text'));
    print(View.btn_Num6.cget('text'));
    
def EnventClick_Number5():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num5.cget('text'));
    print(View.btn_Num5.cget('text'));
    
def EnventClick_Number4():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num4.cget('text'));
    print(View.btn_Num4.cget('text'));
    
    
def EnventClick_Minus():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Minus.cget('text'));
    print(View.btn_Minus.cget('text'));
    
def EnventClick_Number3():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num3.cget('text'));
    print(View.btn_Num3.cget('text'));
    
def EnventClick_Number2():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num2.cget('text'));
    print(View.btn_Num2.cget('text'));
    
def EnventClick_Number1():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num1.cget('text'));
    print(View.btn_Num1.cget('text'));
    
def EnventClick_Multiply():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Multiply.cget('text'));
    print(View.btn_Multiply.cget('text'));
    
def EnventClick_Num0():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num0.cget('text'));
    print(View.btn_Num0.cget('text'));
    
def EnventClick_Num00():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Num00.cget('text'));
    print(View.btn_Num00.cget('text'));
    
def EnventClick_Dot():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_NumDot.cget('text'));
    print(View.btn_NumDot.cget('text'));
    
def EnventClick_Division():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_Division.cget('text'));
    print(View.btn_Division.cget('text'));
    
def EnventClick_Mod():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, Temp + View.btn_NumMod.cget('text'));
    print(View.btn_NumMod.cget('text'));
    
def EnventClick_Result():
    Temp = View.input_Calculator.get();
    View.input_Calculator.delete(0,END);
    View.input_Calculator.insert(INSERT, str(eval(Temp)));