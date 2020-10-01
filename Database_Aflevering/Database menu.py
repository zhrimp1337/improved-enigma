import time
from Database_Aflevering.DatabaseMain import database_Methods
from Database_Aflevering.StockItemClass import StockItemClass
from Database_Aflevering.ArticleClass import ArticleClass
from Database_Aflevering.LocationClass import LocationClass
import Database_Aflevering.Menu_text_functions
import sys


# Database menu for the Warehouse database program
def menu():
    print("************MAIN MENU**************")
    time.sleep(1)

    choice = input(Database_Aflevering.Menu_text_functions.Main_menu_options())  # choice is given whether the user want to edit or show rows in a table, or simply get a whole table printed out

    if choice == "A" or choice == "a":  # The choice is given on what table to operate on
        Table = input(Database_Aflevering.Menu_text_functions.Table_choice_menu())

        if Table == "A" or Table == "a":  # Article table chosen
            Table_option = input(Database_Aflevering.Menu_text_functions.Tablesub_choice_menu())  # The choice is given on what operation the user want to do on the table

            if Table_option == "A" or Table_option == "a":  # Article Insert Menu
                parameters = Database_Aflevering.Menu_text_functions.Article_parameter_options()  # Collect parameters to operate with the instantiation of an ArticleClass
                instance = ArticleClass(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],
                                        parameters[5], parameters[6])
                instance.Article_sql_insert()  # Run the actual sql insert in the Article table with the given parameters
                time.sleep(1)
                print(
                    "Following has been inserted: ArticleID: {} Type: {} Price: {} Colour: {} Weight in grams: {} Make: {} Year: {}".format(
                        parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5],
                        parameters[6]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "B" or Table_option == "b":  # Article Update Menu
                parameters = Database_Aflevering.Menu_text_functions.Article_parameter_options()  # Collect parameters to operate with the instantiation of an ArticleClass
                instance = ArticleClass(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4],
                                        parameters[5], parameters[6])
                instance.Article_sql_update()  # Run the actual sql update in the Article table with the given parameters
                time.sleep(1)
                print(
                    "Following has been updated: ArticleID: {} Type: {} Price: {} Colour: {} Weight in grams: {} Make: {} Year: {}".format(
                        parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5],
                        parameters[6]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "C" or Table_option == "c":  # Article Delete Menu
                parameter = Database_Aflevering.Menu_text_functions.Article_delete_parameter()  # Collect parameters to operate with the instantiation of an ArticleClass
                instance = ArticleClass(parameter, 'cpu', 20, 'blue', 100, 'intel', 2000)  # Phony parameters passed into the instantiation of ArticleClass to make it work
                row = instance.Article_sql_select()  # pull the row to display it after deletion
                instance.Article_sql_delete()  # Run the actual sql delete in the Article table with the given parameters
                time.sleep(1)
                print("Following row has been deleted:" + row)
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "D" or Table_option == "d":  # Article Show rows
                parameter = Database_Aflevering.Menu_text_functions.Article_select_parameter()  # Collect parameters to operate with the instantiation of an ArticleClass
                instance = ArticleClass(parameter, 'cpu', 20, 'blue', 100, 'intel', 2000)  # Phony parameters passed into the instantiation of ArticleClass to make it work
                row = instance.Article_sql_select()  # Run the actual sql select
                print(row)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "Q" or Table_option == "q":
                menu()

        elif Table == "B" or Table == "b":  # Location table chosen
            Table_option = input(Database_Aflevering.Menu_text_functions.Tablesub_choice_menu())  # The choice is given on what operation the user want to do on the table
            if Table_option == "A" or Table_option == "a":  # Location Insert Menu
                parameters = Database_Aflevering.Menu_text_functions.Location_parameter_options()  # Collect parameters to operate with the instantiation of a LocationClass
                instance = LocationClass(parameters[0], parameters[1], parameters[2])
                instance.Location_sql_insert()  # Run the actual sql insert in the Location table with the given parameters
                time.sleep(1)
                print("Following has been inserted: LocationID: {} Line: {} Shelf: {}".format(parameters[0],
                                                                                              parameters[1],
                                                                                              parameters[2]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "B" or Table_option == "b":  # Location Update Menu
                parameters = Database_Aflevering.Menu_text_functions.Location_parameter_options()  # Collect parameters to operate with the instantiation of a LocationClass
                instance = LocationClass(parameters[0], parameters[1], parameters[2])
                instance.Location_sql_update()  # Run the actual sql update in the Location table with the given parameters
                time.sleep(1)
                print(
                    "Following has been updated: LocationID: {} Line: {} Shelf: {}".format(parameters[0], parameters[1],
                                                                                           parameters[2]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "C" or Table_option == "c":  # Location Delete Menu
                parameters = Database_Aflevering.Menu_text_functions.Location_delete_parameter()  # Collect parameters to operate with the instantiation of a LocationClass
                instance = LocationClass(parameters, 2, 2)   # Phony parameters passed into the instantiation of LocationClass to make it work
                row = instance.Location_sql_select()  # pull the row to display it after deletion
                instance.Location_sql_update()  # Run the actual sql delete in the Location table with the given parameters
                time.sleep(1)
                print("Following has been deleted: LocationID:" + row)
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "D" or Table_option == "d":  # Location Show row
                parameter = Database_Aflevering.Menu_text_functions.Location_select_parameter()  # Collect parameters to operate with the instantiation of a LocationClass
                instance = LocationClass(parameter, 2, 2)  # Phony parameters passed into the instantiation of LocationClass to make it work
                row = instance.Location_sql_select()  # Run the actual sql select in the Location table with the given parameters
                print(row)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "Q" or Table_option == "q":  # Back to Main menu
                menu()

        elif Table == "C" or Table == "c": # StockItem table chosen
            Table_option = input(Database_Aflevering.Menu_text_functions.Tablesub_choice_menu())  # The choice is given on what operation the user want to do on the table
            if Table_option == "A" or Table_option == "a":  # StockItem Insert Menu
                parameters = Database_Aflevering.Menu_text_functions.StockItem_parameter_options()  # Collect parameters to operate with the instantiation of a StockItemClass
                instance = StockItemClass(parameters[0], parameters[1], parameters[2])
                instance.StockItem_sql_insert()  # Run the actual sql select in the StockItem table with the given parameters
                time.sleep(1)
                print("Following has been inserted: ArticleID: {} LocationID: {} Amount: {}".format(parameters[0],
                                                                                                    parameters[1],
                                                                                                    parameters[2]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "B" or Table_option == "b":  # StockItem Update Menu
                parameters = Database_Aflevering.Menu_text_functions.StockItem_parameter_options()  # Collect parameters to operate with the instantiation of a StockItemClass
                instance = StockItemClass(parameters[0], parameters[1], parameters[2])
                instance.StockItem_sql_update()  # Run the actual sql update in the StockItem table with the given parameters
                time.sleep(1)
                print("Following has been updated: ArticleID: {} LocationID: {} Amount: {}".format(parameters[0],
                                                                                                   parameters[1],
                                                                                                   parameters[2]))
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "C" or Table_option == "c":  # StockItem Delete Menu
                parameters = Database_Aflevering.Menu_text_functions.StockItem_parameter_options()  # Collect parameters to operate with the instantiation of a StockItemClass
                instance = StockItemClass(parameters[0], parameters[1], 2)   # Phony parameters passed into the instantiation of StockItemClass to make it work
                row = instance.StockItem_sql_select()   # pull the row to display it after deletion
                instance.StockItem_sql_delete()   # Run the actual sql delete in the StockItem table with the given parameters
                time.sleep(1)
                print("Following has been deleted:" + row)
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "D" or Table_option == "d":  # StockItem show menu
                parameter = Database_Aflevering.Menu_text_functions.Location_select_parameter()  # Collect parameters to operate with the instantiation of a StockItemClass
                instance = LocationClass(parameter, 2, 2)  # Phony parameters passed into the instantiation of ArticleClass to make it work
                row = instance.Location_sql_select()    # Run the actual sql delete in the StockItem table with the given parameters
                print(row)
                time.sleep(1)
                input("Press Enter to return to main menu...")
                menu()

            elif Table_option == "Q" or Table_option == "q":  # back to main menu
                menu()

        elif Table == "Q" or Table == "a":
            menu()
    elif choice == "B" or choice == "b":  # Show whole table menu
        print("Which table would you like to view?")
        Table = input(Database_Aflevering.Menu_text_functions.Table_choice_menu())

        if Table == "A" or Table == "a":  # Shows the whole Article table
            instance = Database_Aflevering.DatabaseMain.database_Methods()
            instance.show_table("Article")
            input("Press Enter to return to main menu...")
            menu()

        elif Table == "B" or Table == "b": # Shows the whole Location table
            instance = Database_Aflevering.DatabaseMain.database_Methods()
            instance.show_table("Location")
            input("Press Enter to return to main menu...")
            menu()

        elif Table == "C" or Table == "c": # Shows the whole StockItem table
            instance = Database_Aflevering.DatabaseMain.database_Methods()
            instance.show_table("StockItem")
            input("Press Enter to return to main menu...")
            menu()

        elif Table == "Q" or Table == "q":  # Back to main menu
            menu()

    elif choice == "Q" or choice == "q":  # Exit the program
        sys.exit()

    else:
        print("You must only select either A,B or Q.")
        print("Please try again")
        time.sleep(2)
        menu()


# Program initiated
menu()
