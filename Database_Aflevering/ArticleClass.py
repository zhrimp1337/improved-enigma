from Database_Aflevering.DatabaseMain import database_Methods


class ArticleClass(database_Methods):

    def __init__(self, ArticleID, Type, Price, Colour, WeightGram, Make, Year):
        database_Methods.__init__(self)
        self.ArticleID = ArticleID
        self.Type = Type
        self.Price = Price
        self.Colour = Colour
        self.WeightGram = WeightGram
        self.Make = Make
        self.Year = Year

    def Article_sql_insert(self):
        sql = "INSERT INTO Article (ArticleID,Type,Price,Colour,WeightGram,Make,Year) Values (" + str(self.ArticleID) + ", '" + self.Type + "', " + str(self.Price) + ", '" + self.Colour + "', " + str(self.WeightGram) + ", '" + self.Make + "', " + str(self.Year) + ")"
        self.sql_query(sql)

    def Article_sql_update(self):
        sql = "UPDATE Article SET ArticleID =" + " " + str(self.ArticleID) + ", " + "Type =" + " '" + self.Type + "', " + "Price =" + " " + str(self.Price) + ", " + "Colour =" + " '" + self.Colour + "', " + "WeightGram =" + " " + str(self.WeightGram) + ", " + "Make =" + " '" + self.Make + "', " + "Year =" + " " + str(self.Year) + " " + "WHERE ArticleID =" +" "+ str(self.ArticleID)+""
        self.sql_query(sql)

    def Article_sql_delete(self):
        sql = "DELETE FROM Article WHERE ArticleID =" + " " + str(self.ArticleID)
        self.sql_query(sql)

    def print_object(self):
        print(self.Type)

    def articleupdate(self):
        print("test")

a = ArticleClass(input(), 'cpu', 120, 'grey', 500, 'intel',1997)
#a.Article_sql_update()
#a.Article_sql_insert()
a.Article_sql_delete()


