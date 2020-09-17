from Database_Aflevering.DatabaseMain import database_Methods


class LocationClass(database_Methods):

    def __init__(self, LocationID, Line, Shelf):
        database_Methods.__init__(self)
        self.LocationID = LocationID
        self.Line = Line
        self.Shelf= Shelf

    def Location_sql_insert(self):
        sql = "INSERT INTO Location (LocationID,Line,Shelf) Values (" + str(self.LocationID) + ", '" + str(self.Line) + "', " + str(self.Shelf) + ")"
        self.sql_query(sql)

    def Location_sql_update(self):
        sql = "UPDATE Location SET LocationID =" + " " + str(self.LocationID) + ", " + "Line =" + " " + str(self.Line) + ", " + "Shelf =" + " " + str(self.Shelf) + "WHERE LocationID =" + " " + str(self.LocationID)
        self.sql_query(sql)

    def Location_sql_delete(self):
        sql = "DELETE FROM Location WHERE LocationID =" + " " + str(self.LocationID)
        self.sql_query(sql)

a = LocationClass(2,2,2)
a.Location_sql_insert()
#a.Location_sql_update()
#a.Location_sql_delete()
