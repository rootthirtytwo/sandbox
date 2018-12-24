#Step 1
# pip install virtualenv #To create virtual environments to isolate package installations between projects
# virtualenv venv
# source venv/bin/activate
# pip install pyodbc

#Step 2
#sqlcmd -S localhost -U sa -P your_password -Q "CREATE DATABASE SampleDB;"
# sqlcmd -S localhost -U sa -P your_password -Q "USE SampleDB; CREATE TABLE Employees (Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY, Name NVARCHAR(50), Location NVARCHAR(50));"
# sqlcmd -S localhost -U sa -P your_password -Q "USE SampleDB; INSERT INTO Employees (Name, Location) VALUES (N'Jared', N'Australia'), (N'Nikita', N'India'), (N'Tom', N'Germany');"

import pyodbc
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = 'password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with cursor.execute(tsql,'Jake','United States'):
    print ('Successfuly Inserted!')


#Update Query
print ('Updating Location for Nikita')
tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
with cursor.execute(tsql,'Sweden','Nikita'):
    print ('Successfuly Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Employees WHERE Name = ?"
with cursor.execute(tsql,'Jared'):
    print ('Successfuly Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT Name, Location FROM Employees;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()