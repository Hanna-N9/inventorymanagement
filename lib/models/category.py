from models.__init__ import CURSOR, CONN

class Category:
    
    # Dictionary of objects saved to the database.
    all = {}
    
    #Initialize attributes of the class
    #The id attribute with the default value of None will be assigned a value after saving the object attributes as a new table row.
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    #A special method that provides a string representation for Category class. It returns a string including each attribute of the instance.
    #Example -- Category('Electronics', 1)
    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"
    
    #A class method denoted by the @classmethod decorator. cls is used to execute the SQL command to create the categories table in database. The table has two columns, id and name.
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql) #A SQLite cursor object to execute an SQL command
        CONN.commit() #After the SQL command is executed, this syntax commits the performances/changes to save to the database permanently.
    
    #Drop the categories table from the database if it exist 
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    #Insert a new row into the categories table in database with the value of self.name and update the category instance's id with the id of the newly inserted row.
    #Question mark is placeholders for these (CURSOR.execute) values - Update debug.py to see the result of each print statement of values
    def save(self):
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,)) #Executes the SQL command and second argument to execute is a tuple containing the values to be inserted into the table. 
        CONN.commit()
        self.id = CURSOR.lastrowid #Sets the id attribute of the instance to the ID of the newly inserted row. Lastrowid property of the cursor object returns the ID of the last row that was inserted.
        type(self).all[self.id] = self #Adds the newly created instance to class's all dictionary. Uses the id of the instances as keys and the instances themselves as values. Purpose is to retrieve an instance from the database by its id easily.
     
    #Uses an argument to create a new instance of the Category's class with a given name which then calls save method on this new instance to save it to the database. Finally, it returns the newly created instance.
    #Meaning, this will create a new Category instance with the name 'given name's value' to save it to the database and return the new instance.
    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        return category
    
    
    