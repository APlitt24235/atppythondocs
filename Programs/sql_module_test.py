#Alex Plitt
#Testing EZSQL.py module

#import a .py file from the same folder
import EZSQL

#Creates a database object (See ezsql.py for details)
myDB = EZSQL.EZDB("testdatabase.db")

#Tell the database to run a SELECT Query on classfood table
print(myDB.select("classfood"))

#Run a SELECt query with options (see ezsql.py for details)
print(myDB.select("classfood", columns = "firstname", condition = "height > 60"))
