import pyodbc
from tabulate import tabulate


class database_Methods:  # Create the class which the table classes are supposed to inherit from
    def __init__(self):
        self.conn = self.connect_DB()
        self.cursor = self.conn.cursor()

    def connect_DB(self):  # Define the method for which the class is able to connect to the database
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};' 'Server=localhost;' 'Database=Warehouse;' 'Trusted_Connection=yes;')
        return conn

    def show_table(self, table):  # The show whole table feature of the program
        self.cursor.execute("SELECT * FROM " + table)
        tabledescriptions = []
        tablerows = []
        for row in self.cursor:
            tablerows.append(row)
        for column in self.cursor.description:
            tabledescriptions.append(column[0])

        print(tabulate(tablerows, headers=tabledescriptions))

    def sql_query(self, query, control):  # The sql query function is created with some additional method overloading to not only exectue queries but also retreive data
        if control == None:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            return data

