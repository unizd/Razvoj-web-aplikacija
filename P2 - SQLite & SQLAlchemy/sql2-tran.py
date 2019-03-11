from sqlalchemy import create_engine
db = create_engine('sqlite:///company1.sqlite')

# ispis u konzoli
db.echo = True
conn = db.connect()

# Otvaramo transakciju
trans = conn.begin()

try:
    conn.execute("INSERT INTO Employees VALUES (NULL, 'Mate Jurić', date('1990-09-06') );")
    conn.execute("INSERT INTO Employees VALUES (NULL, 'Ana Horvat', date('1980-09-06') );")
    conn.execute("INSERT INTO Employees VALUES (NULL, 'Pero Ždero', date('1970-07-06') );")
    # Spremamo tek sad sve
    trans.commit()
except:
    # Prolazi sve ili ništa. Ako dođe do greške, sve se poništava
    trans.rollback()
    raise

# vratimo konekciju u "connection pool"
conn.close()