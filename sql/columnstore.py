##SQL Query
# sqlcmd -S localhost -U sa -P Tech@2018 -d SampleDB -t 60000 -Q "WITH a AS (SELECT * FROM (VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)) AS a(a))
# SELECT TOP(5000000)
# ROW_NUMBER() OVER (ORDER BY a.a) AS OrderItemId
# ,a.a + b.a + c.a + d.a + e.a + f.a + g.a + h.a AS OrderId
# ,a.a * 10 AS Price
# ,CONCAT(a.a, N' ', b.a, N' ', c.a, N' ', d.a, N' ', e.a, N' ', f.a, N' ', g.a, N' ', h.a) AS ProductName
# INTO Table_with_5M_rows
# FROM a, a AS b, a AS c, a AS d, a AS e, a AS f, a AS g, a AS h;"

## Result
# Sum: 50000000
# QueryTime: 269621 ms

##Query 2
#sqlcmd -S localhost -U sa -P Tech@2018 -d SampleDB -Q "CREATE CLUSTERED COLUMNSTORE INDEX Columnstoreindex ON Table_with_5M_rows;"

##Result
# Sum: 50000000
# QueryTime: 3409 ms

import pyodbc
from datetime import datetime, time
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = 'password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
tsql = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
a = datetime.now()
with cursor.execute(tsql):
  b = datetime.now()
  c = b - a
  for row in cursor:
    print ('Sum:', str(row[0]))
  print ('QueryTime:', c.microseconds, 'ms')
