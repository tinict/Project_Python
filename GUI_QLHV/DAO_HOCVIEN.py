import ConnectDB

# print(ConnectDB.ConnectDataBase());
connect = ConnectDB.ConnectDataBase();
database = connect.cursor();

def getAll():
    database.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien");
    myresult = database.fetchall();
    return myresult;

def Add_HocVien (Name, Age, Country, Sex, Information, English):
    sql = "insert into Quan_ly_hoc_vien.Hocvien (Name, Age, Country, Sex, Information, English) values (%s, %s, %s, %s, %s, %s)";
    database.execute (sql,(Name, Age, Country, Sex, Information, English));
    connect.commit();
    return 1;
    
def Delete_HocVien(Id):
    sql ="delete from Quan_ly_hoc_vien.Hocvien where Id = %s"
    database.execute (sql,(Id,));
    connect.commit();
    return 1;
    
def Edit_HocVien(Name, Age, Country, Sex, Information, English, Id):
    sql ="update Quan_ly_hoc_vien.Hocvien set Name = %s, Age = %s, Country = %s, Sex = %s, Information = %s, English = %s  where Id = %s";
    database.execute (sql,(Name, Age, Country, Sex, Information, English, Id));
    connect.commit();
    return 1;