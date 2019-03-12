from sqlalchemy import create_engine
db = create_engine('sqlite:///company1.sqlite')

db.echo = True
conn = db.connect()

trans = conn.begin()
try:
    conn.execute("INSERT INTO Addresses (Street, Number, Coordinate, EmployeeID) VALUES ('Trg', 2, '', 1)")
    conn.execute("INSERT INTO Addresses (Street, Number, Coordinat, EmployeeID) VALUES ('Ulica', 2, '', 1)")
    trans.commit()
except:
    trans.rollback()
    raise

conn.close()