
#  Backend-MySQL
#    Sep 05, 2019 06:57:50 PM +0530  platform: Windows-7

'''

import mysql.connector as sql

def studentData():
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    database = 'create database if not exists student'
    cur.execute(database)
    #try:
    table = 'create table if not exists student(id integer primary key,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text'
    cur.execute(table)
    except:
        table = 'create table if not exists mysql.student(id integer primary key,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text'
        cur.execute(table)
    con.commit()
    con.close

def Add(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile ):
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    #try:
    insert = "insert in student(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile ) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    value = [(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile )]
    cur.executemany(insert, value)
    except:
        insert = "insert in mysql.student(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile ) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        value = [(StdID),
                 (Firstname),
                 (Surname),
                 (DoB),
                 (Age),
                 (Gender),
                 (Address),
                 (Mobile)
                 ]
        cur.executemany(insert,value)
    con.commit()
    con.close()

def Display():
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    #try:
    cur.execute('select * from student')
    except:
        cur.execute('select * from mysql.student')
    row = cur.fetchall()
    con.close()
    return row

def Delete(id):
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    try:
        delstate = "delete from student where id = {}".format(id)
        cur.execute(delstate)
    except:
        delstate = "delete from mysql.student where id = {}".format(id)
        cur.execute(delstate)
    con.commit()
    con.close()

def Search(StdID = '',Firstname = '',Surname = '',DoB = '',Age = '',Gender = '',Address = '',Mobile = ''):
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    try:
        serstate = "select * from student where StdID = '{}' or Firstname = '{}' or Surname = '{}' or DoB = '{}' or Age = '{}' or Gender = '{}' or Address = '{}' or Mobile = '{}'"
        cur.execute(serstate.format(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile))
    except:
        serstate = "select * from mysql.student where StdID = '{}' or Firstname = '{}' or Surname = '{}' or DoB = '{}' or Age = '{}' or Gender = '{}' or Address = '{}' or Mobile = '{}'"
        cur.execute(serstate.format(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    row = cur.fetchall()
    con.close
    return row

def Update(id,StdID = '',Firstname = '',Surname = '',DoB = '',Age = '',Gender = '',Address = '',Mobile = ''):
    con = sql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='student'
    )

    cur = con.cursor()
    try:
        upstate = "update student set StdID = '{}' , Firstname = '{}' , Surname = '{}' , DoB = '{}' , Age = '{}' , Gender = '{}' , Address = '{}' , Mobile = '{}' where id = {}"
        cur.execute(upstate.format(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile,id))
    except:
        upstate = "update mysql.student set StdID = '{}' , Firstname = '{}' , Surname = '{}' , DoB = '{}' , Age = '{}' , Gender = '{}' , Address = '{}' , Mobile = '{}' where id = {}"
        cur.execute(upstate.format(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()

'''

#=================================================SQLITE3====================================================================

import sqlite3 as sql

def studentData():
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id integer primary key,StdID text,Firstname text, Surname text,\
    Dob text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

def Add(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile ):
    studentData()
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile))
    con.commit()
    con.close()

def Display():
    studentData()
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    con.close()
    return row

def Delete(id):
    studentData()
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()

def Search(StdID = '',Firstname = '',Surname = '',DoB = '',Age = '',Gender = '',Address = '',Mobile = ''):
    studentData()
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID = ? or Firstname = ? or Surname = ? or DoB = ? or Age = ? or Gender = ? or Address = ? or Mobile = ?",(StdID ,Firstname ,Surname ,DoB ,Age ,Gender ,Address ,Mobile))
    row = cur.fetchall()
    con.close()
    return row

def Update(id,StdID = '',Firstname = '',Surname = '',DoB = '',Age = '',Gender = '',Address = '',Mobile = ''):
    studentData()
    con = sql.connect("Student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID = ? or Firstname = ? or Surname = ? or DoB = ? or Age = ? or \
    Gender = ? or Address = ? or Mobile = ? WHERE id = ?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile,id))
    con.commit()
    con.close()

#===================================================LoginSystem=================================================

def userData():
    con = sql.connect("userdata.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userdata(name text,dob text,email,userID text,gender,passwd text)")
    con.commit()
    con.close()

def create(name,dob,email,user,gender,passwd):
    userData()
    con = sql.connect("userdata.db")
    cur = con.cursor()
    cur.execute("INSERT INTO userdata VALUES (?,?,?,?,?,?)",(name,dob,email,user,gender,passwd))
    con.commit()
    con.close()

def showdata():
    userData()
    con = sql.connect("userdata.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM userdata")
    row = cur.fetchall()
    con.close()
    return row