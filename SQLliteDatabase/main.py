import sqlite3


db = sqlite3.connect("book-collections.db")

cursor = db.cursor()

# Creating table
# cursor.execute("CREATE TABLE BOOKS (id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE, author VARCHAR(250) NOT NULL, rating FLOAT NULL)")
# Insert values
cursor.execute("INSERT INTO BOOKS VALUES(1, 'Harry Poter', 'J. K. Rowling', 4.8)")
db.commit()