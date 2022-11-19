import ConnectDB

# print(ConnectDB.ConnectDataBase());
connect = ConnectDB.ConnectDataBase();
database = connect.cursor();

def getAll():
    database.execute("SELECT * FROM Quan_ly_nhan_vien.NhanVien");
    myresult = database.fetchall();
    return myresult;

def Add_NhanVien (Name, Age, Country, Sex, ChucVu, ChamCong):
    sql = "insert into Quan_ly_nhan_vien.Nhanvien (Name, Age, Country, Sex, ChucVu, ChamCong) values (%s, %s, %s, %s, %s, %s)";
    database.execute (sql,(Name, Age, Country, Sex, ChucVu, ChamCong));
    connect.commit();
    return 1;
def Delete_NhanVien(Id):
    sql ="delete from Quan_ly_nhan_vien.Nhanvien where Id = %s"
    database.execute (sql,(Id,));
    connect.commit();
    return 1;
    
def Edit_NhanVien(Name, Age, Country, Sex, ChucVu, ChamCong, Id):
    sql ="update Quan_ly_nhan_vien.Nhanvien set Name = %s, Age = %s, Country = %s, Sex = %s, ChucVu = %s, ChamCong = %s  where Id = %s";
    database.execute (sql,(Name, Age, Country, Sex, ChucVu, ChamCong, Id));
    connect.commit();
    return 1;