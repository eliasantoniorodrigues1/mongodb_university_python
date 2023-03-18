'''
In this challenge you will use Python to read and write data from a relational
database, and a non-relational database. You will read and write relational
data from a MariaDB database, and interact with non-relational data from a 
MongoDB database. 
You will implement exception handling to deal with common errors that occur 
while accessing data. 
Note: Please ensure that you have set aside enough time to complete the 
challenge lab before you start.

installation:
pip install mariadb

reference:
https://mariadb-corporation.github.io/mariadb-connector-python/usage.html#connecting
'''
import mariadb


# connect to MariaDB
conn_params = {
    "user": "example_user",
    "password": "GHbe_Su3B8",
    "host": "localhost",
    "database": "test"
}
# establish connection
connection = mariadb.connect(**conn_params)
cursor = connection.cursor()

# populating coutries table with some data
cursor.execute('''
INSERT INTO countries(name, country_code, capital) VALUES (?, ?, ?)
''', ('Brazil', 'BRA', 'Brasilia'))

# read data from relational database
cursor.execute('''
SELECT name, country, capital FROM coutries
''')
# print content
row = cursor.fetchone()
print(*row, sep=' ')

# free resources
cursor.close()
connection.cloese()


# interact with non-relational database (MongoDB)
