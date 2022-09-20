#Alex Plitt
#A module for handling SQLite3 queries

import sqlite3

class EZDB():
    #Every class has this method. It runs when an object is made from this class
    def __init__(self, filename):
        #Open the database file, and create a cursor
        self.database = sqlite3.connect(filename)
        self.cursor = self.database.cursor()
    #Define a select method with kwargs
    def select(self, table, columns = "*", condition = ""):
        query = "SELECT " + columns + " FROM " + table
        if condition:
            query += " WHERE " + condition
        query += ";"
        print(query)
        self.cursor.execute(query).fetchall()
    def insert(self, table, values, columns = ""):
        query = "INSERT INTO " + table
        if columns:
            query += " ("
            for column in columns:
                query += '"' + column + '"'
                if not column == columns[-1]:
                    query += ", "
            query += ")"
        query += " VALUES ("
        for value in values:
            if type(value) is str:
                query += '"' + value + '"'
            else:
                query += str(value)
            if not value == values[-1]:
                query += ", "
        query += ");"
        print(query)
        self.cursor.execute(query).fetchall()
        self.database.commit()
    def delete(self, table, condition = ""):
        query = "DELETE FROM " + table + " WHERE " + condition + ";"
        print(query)
        self.cursor.execute(query).fetchall()
        self.database.commit()
    def update(self, table, values, columns, condition):
        query = "UPDATE " + table + " SET "
        for i, value in enumerate(values):
            if type(value) is str:
                query += '"' + columns[i] + '"' + " = " + '"' + value + '"'
            else:
                query += '"' + columns[i] + '"' + " = " + str(value) 
            if not value == values[-1]:
                query += ", "
        query += " WHERE " + condition + ";"
        print(query)
        self.cursor.execute(query).fetchall()
        self.database.commit()

myDB = EZDB("testDataBase.db")

myDB.select("classfood")

myDB.insert("classfood", ["Bob", "Ross", 27, "Paint"], ["firstname", "lastname", "height", "food"])

myDB.delete("classfood", "height < 28")

myDB.update("classfood", ["Alex", "Plitt", 70, "Macaroni"], ["firstname", "lastname", "height", "food"], 'lastname = "Plitt" AND food = "Ramen"')
