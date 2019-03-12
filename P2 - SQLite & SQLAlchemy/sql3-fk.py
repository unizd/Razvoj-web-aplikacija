from sqlalchemy import create_engine
db = create_engine('sqlite:///company1.sqlite')

conn = db.connect()

conn.execute("""
    CREATE TABLE Addresses(
        ID INTEGER PRIMARY KEY,
        Street STRING(100) NOT NULL,
        Number INTEGER,
        Coordinate STRING(255),
        EmployeeID INTEGER NOT NULL,
    FOREIGN KEY(EmployeeID) REFERENCES Employees(ID)
    )""")

trans = conn.begin()
try:
    conn.execute("INSERT INTO Addresses (Street, Number, Coordinate, EmployeeID) VALUES ('Trg', 2, '', 1)")
    conn.execute("INSERT INTO Addresses (Street, Number, Coordinate, EmployeeID) VALUES ('Ulica', 11, '', 2)")
    trans.commit()
except:
    trans.rollback()
    raise

conn.close()