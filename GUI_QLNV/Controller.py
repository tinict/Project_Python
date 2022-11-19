from tkinter import *
import DAO_NHANVIEN
import View
from View import *
import Model
import BO_NHANVIEN

def ShowListener():
    print("Listener Successfull");
    View.boxTextArea.config(state="normal");    
    All_NhanVien = DAO_NHANVIEN.getAll();
    View.boxTextArea.delete('1.0', END);
    for i in All_NhanVien:
        NhanVien = Model.NhanVien(i[0], i[1], i[2], i[3], i[4], i[5], i[6]);
        View.boxTextArea.insert(INSERT, NhanVien.get_NhanVien() + "\n");

def AddListener():
    print("Listener Successfull");
    Compile = 0;
    Compile = DAO_NHANVIEN.Add_NhanVien(View.ip_Name.get(), View.ip_Age.get(), View.ip_Country.get(), BO_NHANVIEN.Sex(View.ip_Sex.get()) , View.ip_ChucVu.get(), View.ip_ChamCong.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã thêm");
    else:
        View.messageBTN.config(text="Thêm không thành công !");
    
def DeleteListener():
    print('Listener Successfull');
    Compile = 0;
    Compile = DAO_NHANVIEN.Delete_NhanVien(View.ip_Id.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã Xóa");
    else:
        View.messageBTN.config(text="Xóa không thành công !");

def UpdateListener():
    print('Listener Successfull');
    Compile = 0;
    Compile = DAO_NHANVIEN.Edit_NhanVien(View.ip_Name.get(), View.ip_Age.get(), View.ip_Country.get(), BO_NHANVIEN.Sex(View.ip_Sex.get()), View.ip_ChucVu.get(), View.ip_ChamCong.get(), View.ip_Id.get());
    if (Compile == 1):
        View.messageBTN.config(text="Đã cập nhật");
    else:
        View.messageBTN.config(text="Cập nhật không thành công !");
    
def CheckConnectDB():
    print('Listener Successfull');
    if (DAO_NHANVIEN.getAll() != ""):
        View.message.config(text="Connect Successfull");
    else:
        View.message.config(text="Disconnect Successfull");