from sqlalchemy import create_engine
db = create_engine('sqlite:///company.sqlite')

# ispis u konzoli
db.echo = True
conn = db.connect()

conn.execute("""
    CREATE TABLE Employees (
        ID INTEGER PRIMARY KEY,
        Name STRING(100) NOT NULL,
        Birthday DATE NOT NULL
    )""")

conn.execute("INSERT INTO employees VALUES (NULL, 'Mate Jurić', date('1990-09-06') );")
conn.execute("INSERT INTO employees VALUES (NULL, 'Ana Horvat', date('1980-09-06') );")
conn.execute("INSERT INTO employees VALUES (NULL, 'Pero Ždero', date('1970-07-06') );")
for row in conn.execute("SELECT * FROM employee"):
    print (row)

# vratimo konekciju u "connection pool"
conn.close()