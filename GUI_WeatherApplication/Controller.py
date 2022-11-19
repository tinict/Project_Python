import View
import GetDataBase

def btnSearch ():
    Data = GetDataBase.DataWeather(View.input_city.get());
    View.label_1.config(text=Data.city + ',' + Data.country);
    View.info_1.config(text=Data.TypeWeather);
    View.info_2.config(text=str(Data.temperature) + ' ' + str(u'\u2103') + '\n' + str(Data.temperature * 1.8 + 32) + ' ' + str(u'\u2109'));
    View.info_3.config(text=Data.humidity);
    View.info_4.config(text=Data.pressure);