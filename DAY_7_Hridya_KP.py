import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root", port="3306", database="student")
mycursor = mydb.cursor()

mycursor.execute("select * from studentDet")
for i in mycursor:
    print(i)
print("connection is ready")

mycursor.execute("update studentDet set age=age+1")

mycursor.execute("select * from studentDet")
for i in mycursor:
    print(i)
print("Updated table")

'''
create database student;
create table studentdet(roll_no int, name varchar(30), address varchar(30), phone int, age int);
insert into studentdet values(1, 'Harsh', 'Delhi', 111111100, 18)
insert into studentdet values(2, 'Pratik', 'Bihar', 11118980, 20)
insert into studentdet values(3, 'Riyanka', 'Siliguri', 118993000, 19)
insert into studentdet values(4, 'Deep', 'Ramnagar', 11111000, 18)
'''