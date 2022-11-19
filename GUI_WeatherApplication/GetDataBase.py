from collections import namedtuple
import json
import requests
from Model import *


response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ 'Hanoi' +"&appid=fe53bfd100e8ca1c2ca47f202a2e9b9c");

def response(name):
    return requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ name +"&appid=fe53bfd100e8ca1c2ca47f202a2e9b9c");

def getInfoData(name, key):
    return response(name).json()[key];

def getObject(name, key1, key2):
    return getInfoData(name, key1)[key2];

def getArrayObject(name, key1, index, key2):
    return getInfoData(name, key1)[index][key2];

def DataWeather(name):
    return Weather(getArrayObject(name, 'weather',0,'description'), int(getObject(name, 'main','temp')-273.13), getObject(name, 'main','humidity'), getObject(name, 'main','pressure'), getObject(name, 'sys','country'), getInfoData(name, 'name'));
