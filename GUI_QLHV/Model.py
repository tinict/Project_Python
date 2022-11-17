from BO_HOCVIEN import *

class Student:
    def __init__(self, id, name, age, city, sex, diemtienganh, diemtin):
        self.id = id;
        self.name = name;
        self.age = age;
        self.city = city;
        self.sex = sex;
        self.diemtin = diemtin;
        self.diemtienganh = diemtienganh;
    def get_HocVien(self):
        return str(self.id) + ' ' + str(self.name) + ' ' + str(self.age) + " " + str(self.city) + " " + str(SexConvert(self.sex)) + " " + str(self.diemtienganh) + " " + str(self.diemtin);