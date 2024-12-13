
import sqlite3

# Connect to the database (or create it)
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

# Create tables for authors and books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        isbn TEXT,
        author_id INTEGER,
        publisher TEXT,
        year INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors (author_id)
    )
''')

# Insert some example data into the authors table
cursor.execute("INSERT INTO authors (first_name, last_name) VALUES ('John', 'Doe')")
cursor.execute("INSERT INTO authors (first_name, last_name) VALUES ('Jane', 'Smith')")

# Insert some example data into the books table
cursor.execute("INSERT INTO books (title, isbn, author_id, publisher, year) VALUES ('Python Programming', '123-4567891234', 1, 'Tech Books', 2020)")
cursor.execute("INSERT INTO books (title, isbn, author_id, publisher, year) VALUES ('Data Science with Python', '234-5678902345', 2, 'Data Press', 2021)")

# Commit the changes
connection.commit()

# Query and display all authors
print("All authors:")
for row in cursor.execute("SELECT * FROM authors"):
    print(row)

# Query and display all books
print("\nAll books:")
for row in cursor.execute("SELECT * FROM books"):
    print(row)

# Query to join authors and books to display book title and author name
print("\nBooks and Authors:")
for row in cursor.execute('''
    SELECT books.title, authors.first_name, authors.last_name
    FROM books
    INNER JOIN authors ON books.author_id = authors.author_id
'''):
    print(row)

# Close the database connection
connection.close()
