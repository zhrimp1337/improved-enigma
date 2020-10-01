
# All the menu oprtions are listed in this document
def Main_menu_options():
    return("""
                      A: Edit Tables or show rows
                      B: Show whole tables
                      Q: Quit

                      Please enter your choice: """)

def Table_choice_menu():
    return("""
                      A: Article
                      B: Location
                      C: StockItem
                      Q: Back to main menu

                      Please enter your choice: """)

def Tablesub_choice_menu():
    return("""
                      A: Insert
                      B: Update
                      C: Delete
                      D: Show rows
                      Q: Back to main menu

                      Please enter your choice: """)
def Article_parameter_options():
        parameters = []
        parameters.append(input("Which ArticleID?"))
        parameters.append(input("Type?"))
        parameters.append(input("Price?"))
        parameters.append(input("Colour?"))
        parameters.append(input("Weight in grams?"))
        parameters.append(input("Make?"))
        parameters.append(input("Year of the model?"))
        return parameters

def Article_delete_parameter():
    ArticleID = input("Which ArticleID is to be deleted?")
    return ArticleID

def Article_select_parameter():
    ArticleID = input("Which ArticleID row would you like to view?")
    return ArticleID


def Location_parameter_options():
        parameters = []
        parameters.append(input("Which LocationID?"))
        parameters.append(input("Line?"))
        parameters.append(input("Shelf?"))
        return parameters

def Location_delete_parameter():
    LocationID = input("Which LocationID is to be deleted?")
    return LocationID

def Location_select_parameter():
    LocationID = input("Which LocationID row would you like to view?")
    return LocationID

def StockItem_parameter_options():
        parameters = []
        parameters.append(input("Which ArticleID?"))
        parameters.append(input("What LocationID?"))
        parameters.append(input("Amount?"))
        return parameters

def StockItem_delete_options():
        parameters = []
        parameters.append(input("Which ArticleID?"))
        parameters.append(input("Which LocationID?"))
        return parameters

