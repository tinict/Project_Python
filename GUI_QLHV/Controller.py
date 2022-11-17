from tkinter import *
import DAO_HOCVIEN
import View
from View import *
import Model
import BO_HOCVIEN

def ShowListener():
    print("Listener Successfull");
    View.boxTextArea.config(state="normal");    
    All_HocVien = DAO_HOCVIEN.getAll();
    View.boxTextArea.delete('1.0', END);
    for i in All_HocVien:
        HocVien = Model.Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]);
        View.boxTextArea.insert(INSERT, HocVien.get_HocVien() + "\n");

def AddListener():
    print("Listener Successfull");
    Compile = 0;
    Compile = DAO_HOCVIEN.Add_HocVien(View.ip_Name.get(), View.ip_Age.get(), View.ip_Country.get(), BO_HOCVIEN.Sex(View.ip_Sex.get()) , View.ip_Information.get(), View.ip_English.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã thêm");
    else:
        View.messageBTN.config(text="Thêm không thành công !");
    
def DeleteListener():
    print('Listener Successfull');
    Compile = 0;
    Compile = DAO_HOCVIEN.Delete_HocVien(View.ip_Id.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã Xóa");
    else:
        View.messageBTN.config(text="Xóa không thành công !");

def UpdateListener():
    print('Listener Successfull');
    Compile = 0;
    Compile = DAO_HOCVIEN.Edit_HocVien(View.ip_Name.get(), View.ip_Age.get(), View.ip_Country.get(), BO_HOCVIEN.Sex(View.ip_Sex.get()), View.ip_Information.get(), View.ip_English.get(), View.ip_Id.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã cập nhật");
    else:
        View.messageBTN.config(text="Cập nhật không thành công !");
    
def CheckConnectDB():
    print('Listener Successfull');
    if (DAO_HOCVIEN.getAll() != ""):
        View.message.config(text="Connect Successfull");
    else:
        View.message.config(text="Disconnect Successfull");