import mysql.connector

def ConnectDataBase ():
  connect = mysql.connector.connect (
      host="localhost",
      user="root",
      password="@Tin18082002",
      database ='Quan_ly_hoc_vien'
  )
  return connect;