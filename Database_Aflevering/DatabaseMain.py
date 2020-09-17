import pyodbc
from tabulate import tabulate


class database_Methods:
    def __init__(self):
        self.conn = self.connect_DB()
        self.cursor = self.conn.cursor()

    def connect_DB(self):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=localhost;'
                              'Database=Warehouse;'
                              'Trusted_Connection=yes;')

        return conn

    def show_table(self, table):
        self.cursor.execute("SELECT * FROM " + table)
        tabledescriptions = []
        tablerows = []
        for row in self.cursor:
            tablerows.append(row)
        for column in self.cursor.description:
            tabledescriptions.append(column[0])

        print(tabulate(tablerows, headers=tabledescriptions))

    def sql_query(self, query):
        self.connect_DB()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

    def print_object(self):
        print(self.conn.getinfo())

