import pyodbc
from tabulate import tabulate
class databasemethods:
    def __init__(self):
        self.conn = self.connectDB()
        self.cursor = self.conn.cursor()

    def connectDB(self):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};' 
        'Server=localhost;'
        'Database=Warehouse;'
        'Trusted_Connection=yes;')

        return conn

    def executeSQL(self,table):
        #self.cursor.execute()
        self.cursor.execute("SELECT * FROM "+table)
        tabledescriptions = []
        tablerows = []
        for row in self.cursor:
            tablerows.append(row)
        for column in self.cursor.description:

             tabledescriptions.append(column[0])

        print(tabulate(tablerows, headers=tabledescriptions))

    Def sql
