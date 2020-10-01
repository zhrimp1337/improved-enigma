import unittest
from Database_Aflevering.DatabaseMain import database_Methods
from Database_Aflevering.StockItemClass import StockItemClass


class DatabaseUnittest(unittest.TestCase):

    def test_conn(self):  # Test the connection to the database
        connection = database_Methods().connect_DB()
        self.assertIsNotNone(connection)
        connection.close()

    def test_InsertAndSelectStockItem(self):  # Test the insert, select and delete against the database with the StockItem class only
        insertedrow = StockItemClass(3,2,10)  # Test is only done with the StockItem class because all three classes use the same methods
        insertedrow.StockItem_sql_insert()
        result = insertedrow.StockItem_sql_select()
        self.assertEqual((insertedrow.ArticleID, insertedrow.LocationID, insertedrow.Amount) , (result.ArticleID, result.LocationID, result.Amount))
        insertedrow.StockItem_sql_delete()
        result2 = insertedrow.StockItem_sql_select()
        self.assertIsNone(result2)

        insertedrow.conn.close()



if __name__ == '__main__':
    unittest.main()
