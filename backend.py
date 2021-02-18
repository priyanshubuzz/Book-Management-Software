import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
        self.conn.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.cursor.execute("SELECT * FROM books WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows 

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def update(self, id, title, author, year,isbn):
        self.cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()