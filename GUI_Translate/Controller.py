from googletrans import Translator
import View
import BO_Translate
from tkinter import *

def text_translator(Text, key):
    translator = Translator();
    translated = translator.translate(Text, dest=key);
    return translated.text;

def translate():
    View.boxTextArea_2.delete(1.0, END);
    print(View.comboBox_2.get());
    lang = View.comboBox_2.get();
    key = BO_Translate.check_Keys(lang);
    text1 = View.boxTextArea_1.get(1.0, END);
    trans = text_translator(text1,key);
    View.boxTextArea_2.insert(INSERT, trans);
    
def Clear():
    View.boxTextArea_1.delete(1.0, END);
    View.boxTextArea_2.delete(1.0, END);
