import BO_SoDe
import View
from tkinter import *

def getMemory(temp):
    str = '';
    for i in temp:
        str += i + ' ';
    return str;

def FindWin(str, temp):
    for i in temp:
        if (str == temp):
            return str.length();
    return 0;

def ResultXoSoLo():
    ip1 = View.ip_1.get();
    View.boxTextArea.config(state=NORMAL);
    View.boxTextArea.delete('1.0', END);
    BO_SoDe.GiaiDD(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.GiaiDD(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai1(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai1(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai2(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai2(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai3(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai3(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai4(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai4(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai5(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai5(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai6(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai6(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai7(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai7(BO_SoDe.Nums)) + "\n");
    if (FindWin(ip1, BO_SoDe.Memory) == 0):
        View.val5.set(str(int(View.val5.get()) - int(View.val1.get()) * 23000 * int(View.val2.get())));
    else:
        View.val5.set(str(int(View.val5.get()) + int(View.val1.get()) * 23000 * int(View.val2.get()))); 
    View.val1.set('');
    View.val2.set(''); 

def ResultXoSoDe():
    ip3 = View.ip_3.get();
    View.boxTextArea.config(state=NORMAL);
    View.boxTextArea.delete('1.0', END);
    BO_SoDe.GiaiDD(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.GiaiDD(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai1(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai1(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai2(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai2(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai3(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai3(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai4(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai4(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai5(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai5(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai6(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai6(BO_SoDe.Nums)) + "\n");
    BO_SoDe.Giai7(BO_SoDe.Nums);
    View.boxTextArea.insert(INSERT, getMemory(BO_SoDe.Giai7(BO_SoDe.Nums)) + "\n");
    if (FindWin(ip3, BO_SoDe.Memory) == 0):
        View.val5.set(str(int(View.val5.get()) - int(str(View.val3.get())) * 23000 * int(View.val4.get())));
    else:
        View.val5.set(str(int(View.val5.get()) + int(str(View.val3.get())) * 1000 * int(View.val4.get())));  
    View.val3.set('');
    View.val4.set('');                             