import pyodbc
class databasemethods:
    def __init__(self):
        self.cursor = self.connectDB()

    def connectDB(self):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
        'Server=localhost;'
        'Database=Warehouse;'
        'Trusted_Connection=yes;')

        return conn.cursor()

    def executeSQL(self,table):
        self.cursor.execute("SELECT * FROM "+table)

        for row in self.cursor:
            print(row)

Instance1 = databasemethods()
Instance1.executeSQL("Article")
