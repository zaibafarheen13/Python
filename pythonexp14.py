import sqlite3
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

def Display_Data(db,table):
  try:
    #connect with the myTable database
    connection=sqlite3.connect(db)

    #cursor object
    crsr=connection.cursor()

    #execute the command to fetch all the data from the table emp
    crsr.execute("SELECT * FROM "+table)

    #store all the fetched data in the ans variable
    ans=crsr.fetchall()

    #Since we have already selected all the data entries
    #Using the "SELECT *" SQL command and stored them in
    #the ans variable, all we need to do is to print
    #out the ans variable

    for i in ans:
      print(i)
  except Exception as e:
    print("Exception raised is:",e)

#creating the database
try:
  #connecting to the database and it will create a database if it doesn't exist and then connect to it
  connection=sqlite3.connect("Demo_DataBase.db")

  #cursor
  crsr=connection.cursor()

  #print statement will execute if there are no errors
  print("Connected to the database")

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
  connection.close()
except Exception as e:
  print("Exception raised is:",e)
