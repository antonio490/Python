import sqlite3

# create a connection
conn = sqlite3.connect('cars.db')

# create a cursor
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS cars""")

c.execute("""CREATE TABLE cars (
            name TEXT,
            model TEXT,
            year INTEGER
    )""")

# insert data into a table
c.execute("INSERT INTO cars VALUES ('AUDI', 'A3', 2013)")

all_students = [
    ('BMW', 'M3', 2010),
    ('Mercedes', 'C220', 2018),
    ('Opel', 'Astra', 2020),
]
c.executemany("INSERT INTO cars VALUES (?, ?, ?)", all_students)

# select data
c.execute("SELECT * FROM cars")
print(c.fetchall())

# commit
conn.commit()

# close the connection
conn.close()


# References
# 1. https://medium.com/towards-data-science/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3