import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
insert_table = "INSERT INTO users (id, username, password) VALUES ('3', 'Jack', 'Bhaskar@123')"
#cursor.execute(create_table)
cursor.execute(insert_table)
connection.commit()
connection.close()