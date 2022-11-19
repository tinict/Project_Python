from tkinter import scrolledtext
import Controller
from Controller import *
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 

GUI = Tk();
GUI.title('Currency Converter');
GUI.geometry('700x600');

def main_ConvertCurrency ():
    GUI.mainloop();
    
tkinter.Label (GUI, text= "Amount", fg="black").grid(column=0, row=0, padx=10, pady=10);
tkinter.Label (GUI, text= "USD Currency Converter Using Python", fg="black").grid(column=2, row=0, padx=10, pady=10);

ip_1 = tkinter.Entry(GUI);
ip_1.grid(column=0, row=1, padx=10, pady=10);

pilImage = Image.open("D:\WorkSpace\Project\Python_Project_BKACAD\GUI_ConvertCurrency\img\cur.png").resize((100,100));
test = ImageTk.PhotoImage(pilImage);
label_img = tkinter.Label(image=test);
label_img.image = test;
label_img.grid(column=2,row=2, padx=10, pady=20);

combobox1 = ttk.Combobox(GUI);
combobox1.grid(column=3, row=1, padx=10, pady=10);
combobox1['values'] = 'USD';

ip_1 = tkinter.Entry(GUI);
ip_1.grid(column=0, row=3, padx=10, pady=10);

combobox1 = ttk.Combobox(GUI);
combobox1.grid(column=3, row=3, padx=10, pady=10);
combobox1['values'] = (
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTC",
    "BTN",
    "BWP",
    "BYN",
    "BYR",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "USDDZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "GBP",
    "GEL",
    "GGP",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "IMP",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JEP",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KPW",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LTL",
    "LVL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRO",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLE",
    "SLL",
    "SOS",
    "SRD",
    "STD",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "UYU",
    "UZS",
    "VEF",
    "VES",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XAG",
    "XAU",
    "XCD",
    "XDR",
    "XOF",
    "XPF",
    "YER",
    "ZAR",
    "ZMK",
    "ZMW",
    "ZWL" 
)

btnSearch = tkinter.Button(GUI, text="Search", background="white", width=10);
btnSearch.grid(column=0, row=4, padx=10, pady=10)

btnClear= tkinter.Button(GUI, text="Search", background="white", width=10);
btnClear.grid(column=0, row=5, padx=10, pady=10);

boxmessage = tkinter.Text(GUI, width=40, height=10);
boxmessage.grid(columnspan=3, ipadx=5, column=1, row=5);