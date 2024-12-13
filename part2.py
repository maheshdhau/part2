
import sqlite3

# Connect to the database file
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# Display all the tables in the database
print("Tables in the database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for table in cursor.fetchall():
    print(table[0])

# Query 1: Display all records from the authors table
print("\nAll records from the authors table:")
for row in cursor.execute("SELECT * FROM authors;"):
    print(row)

# Query 2: Display all records from the titles table ordered by title
print("\nAll records from the titles table ordered by title:")
for row in cursor.execute("SELECT * FROM titles ORDER BY title;"):
    print(row)

# Query 3: Inner join authors and titles on the ISBN
print("\nAuthors and titles joined on ISBN:")
query = """
SELECT first, last, title FROM authors 
INNER JOIN author_ISBN ON authors.id = author_ISBN.author_id 
INNER JOIN titles ON author_ISBN.isbn = titles.isbn;
"""
for row in cursor.execute(query):
    print(row)

# Close the database connection
connection.close()
