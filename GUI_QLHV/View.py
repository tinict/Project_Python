from tkinter import scrolledtext
import Controller
from Controller import *
import tkinter
from tkinter import *
from tkinter import ttk

GUI = Tk();
GUI.title('Quản lý học viên - PythonBKACAD');
GUI.geometry('500x740');

def main_QLSV ():
    GUI.mainloop();

tkinter.Label (GUI, text= "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", fg="black").grid(column=4, row=0, padx=10, pady=10);

tkinter.Label (GUI, text= "Name", fg="black").grid(column=2, row=1, padx=10, pady=10);
ip_Name = tkinter.Entry(GUI, width=30);
ip_Name.grid(column=4, row=1, padx=10, pady=10);

tkinter.Label (GUI, text= "Age", fg="black").grid(column=2, row=2, padx=10, pady=10);
ip_Age = tkinter.Entry(GUI, width=30);
ip_Age.grid(column=4, row=2, padx=10, pady=10);

tkinter.Label (GUI, text= "Country", fg="black").grid(column=2, row=3, padx=10, pady=10);
ip_Country = tkinter.Entry(GUI, width=30);
ip_Country.grid(column=4, row=3, padx=10, pady=10);

tkinter.Label (GUI, text= "Sex", fg="black").grid(column=2, row=4, padx=10, pady=10);
ip_Sex = ttk.Combobox(GUI, width=27);
ip_Sex['values'] = ('Male', 'Female', 'Unknown');
ip_Sex.grid(column=4, row=4, padx=10, pady=10);

tkinter.Label (GUI, text= "Information", fg="black").grid(column=2, row=5, padx=10, pady=10);
ip_Information = tkinter.Entry(GUI, width=30);
ip_Information.grid(column=4, row=5, padx=10, pady=10);

tkinter.Label (GUI, text= "English", fg="black").grid(column=2, row=6, padx=10, pady=10);
ip_English = tkinter.Entry(GUI, width=30);
ip_English.grid(column=4, row=6, padx=11, pady=10);

#BTN Thêm học viên
btn_Add = tkinter.Button(GUI, text="Thêm học viên", command=Controller.AddListener);
btn_Add.grid(column=2, row=7, padx=10, pady=10);

# BTN Hiển thị danh sách học viên
btn_Show = tkinter.Button(GUI, text="Hiển thị học viên", command=Controller.ShowListener);
btn_Show.grid(column=4, row=7, padx=10, pady=10);

# input id học viên
tkinter.Label (GUI, text= "Id học viên", fg="black", bg="white").grid(column=2, row=8, padx=10, pady=10);
ip_Id = tkinter.Entry(GUI, width=20);
ip_Id.grid(column=4, row=8, padx=10, pady=10);

# BTN Xóa học viên
btn_Delete = tkinter.Button(GUI, text="Xóa học viên", command=Controller.DeleteListener);
btn_Delete.grid(column=2, row=9, padx=10, pady=10);

# BTN Sửa học viên
btn_Edit = tkinter.Button(GUI, text="Sửa học viên", command=Controller.UpdateListener);
btn_Edit.grid(column=4, row=9, padx=10, pady=10);

# message 
messageBTN = tkinter.Label (GUI, text= "", fg="black");
messageBTN.grid(column=4, row=10, padx=10, pady=10);

# Text area hiển thị danh sách
boxTextArea = scrolledtext.ScrolledText(GUI, wrap = tkinter.WORD, width = 40, height = 10);
boxTextArea.grid(column=4, row=11, padx=10, pady=10);
boxTextArea.config(state=DISABLED);

# BTN connect
btn_ConnectDataBase = tkinter.Button(GUI, text="Kiểm tra kết nối", command=Controller.CheckConnectDB);
btn_ConnectDataBase.grid(column=4, row=12, padx=10, pady=10);

message = tkinter.Label (GUI, text= "", fg="black");
message.grid(column=4, row=13, padx=10, pady=10);