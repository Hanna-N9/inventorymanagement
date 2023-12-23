from models.__init__ import CURSOR, CONN

class Category:
    
    # Dictionary of objects saved to the database.
    all = {}
    
    #Initialize attributes of the class
    #The id attribute with the default value of None will be assigned a value after saving the object attributes as a new table row.
    def __init__(self, name, sub_category, id=None):
        self.id = id
        self.name = name
        self.sub_category = sub_category
    
    #A special method that provides a string representation for Category class. It returns a string including each attribute of the instance.
    #Example -- Category('Electronics', 'TV', 1)
    def __repr__(self):
        return f"<Category {self.id}: {self.name}, {self.sub_category}>"
    
    #A class method denoted by the @classmethod decorator. cls is used to execute the SQL command to create the categories table in database    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
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
        
    #Insert a new row into the categories table in database with the values of self.name and self.sub_category and update id attribute of the category instance with the id of the newly inserted row.
    #Question marks are placeholders for these (CURSOR.execute) values - Update debug.py to see the result of each print statement of values
    def save(self):
        sql = """
            INSERT INTO categories (name, sub_category)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.sub_category)) #Executes the SQL command and second argument to execute is a tuple containing the values to be inserted into the table. 
        CONN.commit()
        self.id = CURSOR.lastrowid #Sets the id attribute of the instance to the ID of the newly inserted row. Lastrowid property of the cursor object returns the ID of the last row that was inserted.
        type(self).all[self.id] = self #Adds the newly created instance to a dictionary belonging to the class. Uses the id of the instances as keys and the instances themselves as values. Purpose to retrieve an instance from the database by its id easily.
        
    #Uses the two arguments to create a new instance of the Category class which then calls save method on this new instance to save it to the database. At the end, it returns the newly created instance.
    #Meaning, this will create a new Category instance with the name 'named value' and sub_category 'named valued' to save it to the database and return the new instance.
    @classmethod
    def create(cls, name, sub_category):
        category = cls(name, sub_category)
        category.save()
        return category
    
    