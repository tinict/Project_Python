import tkinter
from tkinter import *
from tkinter import ttk
import Controller
from PIL import ImageTk, Image 
from datetime import date

GUI = Tk();
GUI.title('Weather Application');
GUI.geometry('1180x500');

def main_Weather_Application():
    GUI.mainloop();
    
today = date.today();

label_1 = tkinter.Label(GUI, text='NA-/', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_1.grid(column=0, row=0);

label_2_2 = tkinter.Label(GUI, text=today.strftime("%Y") + '-' + today.strftime("%m") + '-' + today.strftime("%d"), background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_2_2.grid(column=4, row=0);

label_2 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_2.grid(column=1, row=0);

label_2_1 = tkinter.Label(GUI, text='Weather Report', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_2_1.grid(column=2, row=0);

label_2 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=25, height=2);
label_2.grid(column=3, row=0);

pilImage = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_WeatherApplication\img\wearherapp.png").resize((100,100));
test = ImageTk.PhotoImage(pilImage);

label_3 = tkinter.Label(image=test); 
label_3.image = test;
label_3.grid(column=0,row=1, padx=10, pady=20, rowspan=4, ipadx=4);

tkinter.Label(GUI, text='City or Country Name', font=("Arial", 12)).grid(column=2,row=1);

input_city = tkinter.Entry(GUI, font=15);
input_city.grid(column=2,row=2);

button_Search = tkinter.Button(GUI, text="Search", background='white', fg='black', width=15, command=Controller.btnSearch);
button_Search.grid(column=3,row=2);

label_4 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_4.grid(column=0, row=6);

label_5 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_5.grid(column=1, row=6);

label_5 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=25, height=2);
label_5.grid(column=3, row=6);

label_e1 = tkinter.Label(GUI, text='', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_e1.grid(column=4, row=6);

label_e2 = tkinter.Label(GUI, text='Weather Report', background="blue", fg="white", font=("Arial", 15), width=20, height=2);
label_e2.grid(column=2, row=6);

pilImage2 = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_WeatherApplication\img\clouds.png").resize((100,100));
test2 = ImageTk.PhotoImage(pilImage2);

label_6 = tkinter.Label(image=test2);
label_6.image = test2;
label_6.grid(column=1,row=7, padx=10, pady=20);

info_1 = tkinter.Label(GUI, text='NA/-', font=(16));
info_1.grid(column=1, row=8);

pilImage3 = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_WeatherApplication\img\climate.png").resize((100,100));
test3 = ImageTk.PhotoImage(pilImage3);

label_7 = tkinter.Label(image=test3);
label_7.image = test3;
label_7.grid(column=2,row=7, padx=10, pady=20);

info_2 = tkinter.Label(GUI, text='NA/-', font=(16));
info_2.grid(column=2, row=8);

pilImage4 = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_WeatherApplication\img\mua.png").resize((100,100));
test4 = ImageTk.PhotoImage(pilImage4);

label_8 = tkinter.Label(image=test4);
label_8.image = test4;
label_8.grid(column=3,row=7, padx=10, pady=20);

info_3 = tkinter.Label(GUI, text='NA/-', font=(16));
info_3.grid(column=3, row=8);

pilImage5 = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_WeatherApplication\img\wind.png").resize((100,100));
test5 = ImageTk.PhotoImage(pilImage5);

label_9 = tkinter.Label(image=test5);
label_9.image = test5;
label_9.grid(column=4,row=7, padx=10, pady=20);

info_4 = tkinter.Label(GUI, text='NA/-', font=(16));
info_4.grid(column=4, row=8);