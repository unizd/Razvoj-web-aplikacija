from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///company-orm.sqlite')
engine.echo = True

# temeljna klasa za naše modele
Base = declarative_base()

# sesija vezana uz "engine"
Session = sessionmaker(bind=engine)
session = Session()

# prvi model
class Address(Base):
    # naziv tablice u bazi
    __tablename__ = 'Addresses'
    # primarni ključ
    ID = Column(Integer, primary_key=True)
    Street = Column(String(100))
    Number = Column(Integer)
    Coordinate = Column(String(255))
    # strani ključ
    EmployeeID = Column(Integer, ForeignKey('Employees.ID'))
    
    def __repr__(self):
        return u"%s, %d" % (self.Street, self.Number)

class Employee(Base):
    __tablename__ = 'Employees'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Birthday = Column(Date)
    # mapiramo adrese
    Addresses = relationship("Address", backref="Employees")
    def __repr__(self):
        return self.Name

# kreiramo bazu iz modela
Base.metadata.create_all(engine)

# unos unutar jedne transakcije
session.add_all([
    Employee(Name='Mate Jurić', Birthday=datetime.strptime('1990-09-06', '%Y-%m-%d')),
    Employee(Name='Rosa Petrić', Birthday=datetime.strptime('1980-09-06', '%Y-%m-%d')),
    Employee(Name='Vinka Horvat', Birthday=datetime.strptime('1970-07-06', '%Y-%m-%d'))
    ])
session.commit()

session.add_all([
    Address(Street='Kalelarga', Number=3, Coordinate='', EmployeeID=1),
    Address(Street='Bulevar', Number=7, Coordinate='', EmployeeID=1),
    Address(Street='Forum', Number=10, Coordinate='44.114167,15.227778', EmployeeID=2)
])
session.commit()

# Dohvati Matu, pa onda njegove adrese
marcos = session.query(Employee).filter(Employee.Name.like(r"%Mate%")).first()
for address in marcos.Addresses:
    print ('Address:', address)