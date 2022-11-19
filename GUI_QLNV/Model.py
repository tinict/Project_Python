from BO_NHANVIEN import *

class NhanVien:
    def __init__(self, id, name, age, city, sex, ChucVu, ChamCong):
        self.id = id;
        self.age =  age;
        self.name = name;
        self.city = city;
        self.ChucVu = ChucVu;
        self.sex = sex;
        self.ChamCong = ChamCong;
    def get_NhanVien(self):
        return str(self.id) + ' ' + str(self.name) + ' ' + str(self.age) + " " + str(self.city)  + " " + str(SexConvert(self.sex)) + " " + str(self.ChucVu) + " " + str(self.ChamCong);