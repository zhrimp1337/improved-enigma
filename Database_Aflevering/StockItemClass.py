from Database_Aflevering.DatabaseMain import database_Methods


class StockItemClass(database_Methods):

    def __init__(self, ArticleID, LocationID, Amount):
        database_Methods.__init__(self)
        self.ArticleID = ArticleID
        self.LocationID = LocationID
        self.Amount= Amount

    def StockItem_sql_insert(self):
        sql = "INSERT INTO StockItem (ArticleID,LocationID,Amount) Values (" + str(self.ArticleID) + ", '" + str(self.LocationID) + "', " + str(self.Amount) + ")"
        self.sql_query(sql)

    def StockItem_sql_update(self):
        sql = "UPDATE StockItem SET LocationID =" + " " + str(self.LocationID) + ", " + "Line =" + " " + str(self.Line) + ", " + "Shelf =" + " " + str(self.Shelf) + "WHERE LocationID =" + " " + str(self.LocationID)
        self.sql_query(sql)

    def StockItem_sql_delete(self):
        sql = "DELETE FROM StockItem WHERE ArticleID =" + " " + str(self.LocationID)
        self.sql_query(sql)

a = StockItemClass(2,2,2)
a.StockItem_sql_insert()
