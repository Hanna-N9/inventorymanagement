from models.__init__ import CURSOR, CONN

class Category:
    
    #Initialize attributes of the class
    #The id attribute with the default value of None will be assigned a value after saving the object attributes as a new table row.
    def __init__(self, category_name, sub_category, id=None):
        self.id = id
        self.category_name = category_name
        self.ub_category = ub_category
    
    #A special method that provides a string representation for Category class. It returns a string including each attribute of the instance.
    #Example -- Category('Electronics', 'TV', 1)
    def __repr__(self):
        return f"<Category {self.id}: {self.category_name}, {self.ub_category}>"
    
    #A class method denoted by the @classmethod decorator. cls is used to execute the SQL command to create the categories table in database    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            category_name TEXT,
            sub_category TEXT
            )
        """
        CURSOR.execute(sql) #A SQLite cursor object to execute an SQL command
        CONN.commit() #After the SQL command is executed, this syntax commits the performances/changes to save to the database permanently.
    
    #Drop/Delete a table from a database if it exist 
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()

