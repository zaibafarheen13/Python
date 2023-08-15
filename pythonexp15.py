#pgm15
import sqlite3

def Display_Data(db,table):
  #connect with mytable database

  connection=sqlite3.connect(db)

    #cursor object
  crsr=connection.cursor()

    #execute the command to fetch all the data from the table emp
  crsr.execute("SELECT * FROM "+table)

    #store all fetched data in the ans variable
  ans=crsr.fetchall()

    #Since we have already selected all the data entries
    #Using the "SELECT *" SQL command and stored them in
    #the ans variable, all we need to do is to print
    #out the ans variable

  for i in ans:
     print(i)

def Insert_Data(db_name,sql_command):
  try:
    #connecting to the database
    connection=sqlite3.connect(db_name)

    #cursor
    crsr=connection.cursor()
    crsr.execute(sql_command)

    #To save the changes in the files. Never skip this.
    #If we skip this, nothing will be saved in the database.

    connection.commit()

    #close the connection
    connection.close()

  except sqlite3.Error as e:
    print("Exception raised is:",e)

#creating the database
#connecting to the database and it will create a database if it doesn't exist and then connect to it
connection=sqlite3.connect("Demo_DataBase.db")

#cursor
crsr=connection.cursor()

#print statement will execute if there are no errors
print("Connected to the database")

#SQL command to create a table in the database
sql_command="""CREATE TABLE emp_details_table2(
  staff_number INTEGER PRIMARY KEY,
  mobile VARCHAR(10),
  email VARCHAR(30));"""

#execute the statement
crsr.execute(sql_command)

print("Database after Inserting into the data...")


sql_command1="""INSERT INTO emp_details_table2 VALUES (23,"9876543210","Bansa@gmail.com");"""
Insert_Data("Demo_DataBase.db",sql_command1)

sql_command2="""INSERT INTO emp_details_table2 VALUES (1,"8975461230","Gates@gmail.com");"""
Insert_Data("Demo_DataBase.db",sql_command2)

Display_Data("Demo_DataBase.db","emp_details_table2")

#close connection
crsr=connection.cursor()

#print statement will execute if there are no errors
print("Connected to database")

#tmp='''DROP TABLE Join_demo;'''
#crsr.execute(tmp)
#connection.commit()
#Creating the database
#connecting to the database and it will create a database if it doesn't exist and then connects to it

connection=sqlite3.connect("Demo_DataBase.db")

#SQL command to create a table in the database
sql_command="""CREATE TABLE emp_table1(
  staff_number INTEGER PRIMARY KEY,
  fname VARCHAR(20),
  lname VARCHAR(30));"""

#execute the statement
crsr.execute(sql_command)

print("Database after Inserting into the data...")


sql_command1="""INSERT INTO emp_table1 VALUES (23,"Rishab","Bansal");"""
Insert_Data("Demo_DataBase.db",sql_command1)

sql_command2="""INSERT INTO emp_table1 VALUES (1,"Bill","Gates");"""
Insert_Data("Demo_DataBase.db",sql_command2)

Display_Data("Demo_DataBase.db","emp_table1")

#close the connection
#connection.close()

join_str2='''CREATE TABLE Join_Demo as SELECT emp_table1.fname,emp_details_table2.mobile
FROM emp_table1 INNER JOIN emp_details_table2
ON emp_table1.staff_number=emp_details_table2.staff_number;'''
crsr.execute(join_str2)
connection.commit()

Display_Data("Demo_DataBase.db","Join_Demo")
crsr.close()
