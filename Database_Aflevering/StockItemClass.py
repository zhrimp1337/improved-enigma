from Database_Aflevering.DatabaseMain import database_Methods


class StockItemClass(database_Methods):  # Inherits from database_methods in order to make sql queries

    def __init__(self, ArticleID, LocationID, Amount):
        database_Methods.__init__(self)
        self.ArticleID = ArticleID
        self.LocationID = LocationID
        self.Amount= Amount

    def StockItem_sql_insert(self):
        sql = "INSERT INTO StockItem (ArticleID,LocationID,Amount) Values (" + str(self.ArticleID) + ", '" + str(self.LocationID) + "', " + str(self.Amount) + ")"
        self.sql_query(sql, None)

    def StockItem_sql_update(self):
        sql = "UPDATE StockItem SET LocationID =" + " " + str(self.LocationID) + ", " + "ArticleID =" + " " + str(self.ArticleID) + ", " + "Amount =" + " " + str(self.Amount) + "WHERE LocationID =" + " " + str(self.LocationID)
        self.sql_query(sql, None)

    def StockItem_sql_delete(self):
        sql = "DELETE FROM StockItem WHERE ArticleID =" + " " + str(self.ArticleID) + "AND LocationID =" + " " + str(self.LocationID)
        self.sql_query(sql, None)

    def StockItem_sql_select(self):
        sql = "SELECT * FROM StockItem Where ArticleID =" + " " + str(self.ArticleID)
        row = self.sql_query(sql, True)
        return row
