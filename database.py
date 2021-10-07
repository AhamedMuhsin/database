# importing pymysql for using our dataspace
import pymysql

# making create connection to connect our program to dataspace
def create():
    return pymysql.connect(host="localhost", database="ahamed muhsin", user="root",
                           password="", port=3306)

# making a function to create a table in our dataspace
def Createtable():
    conn = create()
    cursor = conn.cursor()
    query = "create table student(rollno int primary key auto_increment, name VARCHAR(50), email VARCHAR(50), city VARCHAR(50))"
    cursor.execute(query)
    conn.commit()
    print("Table Created")
    conn.close()

# Createtable()

# making a function to insert all our things in table
def InsertData(name , email, city):
    conn = create()
    cursor = conn.cursor()
    args = (name, email, city)
    query = "insert into student(name, email, city)values(%s, %s, %s)"
    cursor.execute(query, args)
    conn.commit()
    print("Data Inserted")
    conn.close()

# name = input("Enter Your Name : ")
# email = input("Enter Your Email : ")
# city = input("Enter Your City : ")

# InsertData(name, email, city)

def showalldata():
    conn = create()
    cursor = conn.cursor()
    query = "select * from student"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)

# showalldata()

def fetchdatabyid(rollno):
    conn = create()
    cursor = conn.cursor()
    args = (rollno)
    query = "select * from student where rollno=%s"
    cursor.execute(query, args)
    result = cursor.fetchall()
    for i in result:
        print(i)

# rollno = int(input("Enter a rollno :"))
# fetchdatabyid(rollno)

# making a data update function for update a data in database
def dataupdate(name, email, city, rollno):
    conn = create()
    cursor = conn.cursor()
    args = (name, email, city, rollno)
    query = "update student set name=%s, email=%s, city=%s where rollno=%s"
    cursor.execute(query, args)
    conn.commit()
    print("Data Updated")
    conn.close()

# showalldata()
#
# rollno = int(input("Enter Your Rollno :"))
# name = input("Enter Your Name : ")
# email = input("Enter Your email : ")
# city = input("Enter Your city : ")
#
# dataupdate(name, email, city, rollno)
#
# showalldata()

# making a delete function to delete function from database
def deleteData(rollno):
    conn = create()
    cursor = conn.cursor()
    args = (rollno)
    query = "delete from student where rollno=%s"
    cursor.execute(query, args)
    conn.commit()
    print("Delete data")
    conn.close()

showalldata()

rollno = int(input("Enter Your Rollno : "))
deleteData(rollno)

showalldata()