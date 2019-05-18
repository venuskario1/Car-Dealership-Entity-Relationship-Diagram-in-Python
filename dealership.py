from sqlalchemy import create_engine,Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base #saves us from writing out the class users (oobject)
from sqlalchemy.orm import sessionmaker, relationship
#create engine will grab a hold of AWS url
# String class will equate to VARCHAR in our PostGres

db_string = "postgres://Kario:u21neq92gei@car-dealership.cib0pjw76th1.us-east-2.rds.amazonaws.com:5432/car_dealer"

db = create_engine(db_string) #engine for database - creates the connection between local machine and aws-server, create connection to database

Base = declarative_base() #upper case letter in variable shows this is a class we are using

# Creation of Database Models for Object Relational Mapper -- ORM

class Salesperson(Base):
    __tablename__ = 'salesperson'

    sales_person_id = Column(Integer, primary_key=True)
    sales_person_name = Column(String(50))
    car = relationship("Car",backref="salesperson")
    payment = relationship("Payment",backref="salesperson")

class Car(Base):
    __tablename__ = 'car'
    
    car_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    sales_person_id = Column(Integer, ForeignKey('salesperson.sales_person_id'))
    service_id = Column(Integer, ForeignKey('service.service_id'))
    servicehistory = relationship("Servicehistory", backref="car") 

class Customer(Base):
    __tablename__ = 'customer'
    
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(50))
    car = relationship("Car", backref="customer")
    payment = relationship("Payment", backref="customer") 

class Mechanics(Base):
    __tablename__ = 'mechanics'
    
    mechanic_id = Column(Integer, primary_key=True)
    mechanic_name = Column(String(50))
    service = relationship("Service", backref="mechanics") 

class Payment(Base):
    __tablename__ = 'payment'
    
    payment_id = Column(Integer, primary_key=True)
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    sales_person_id = Column(Integer, ForeignKey('salesperson.sales_person_id'))
    servicehistory = relationship("Servicehistor",backref="payment")

class Inventory(Base):
    __tablename__ = 'inventory'
    
    inventory_id = Column(Integer, primary_key=True)
    payment = relationship("Payment",backref="inventory")

class Parts(Base):
    __tablename__ = 'carparts'
    
    parts_id = Column(Integer, primary_key=True)
    address_id = Column(String)
    service = relationship("Service", backref="parts")

class Service(Base):
    __tablename__ = 'service'
    
    service_id = Column(Integer, primary_key=True)
    mechanic_id = Column(Integer, ForeignKey('mechanics.mechanic_id'))
    parts_id = Column(Integer, ForeignKey('carparts.parts_id'))
    car = relationship("Car",backref="service")
    serviceticket = relationship("Serviceticket",backref="service")

class Servicehistory(Base):
    __tablename__ = 'servicehistory'
    
    service_history_id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('car.car_id'))
    payment_id = Column(Integer, ForeignKey('payment.payment_id'))

class Serviceticket(Base):
    __tablename__ = 'serviceticket'
    
    service_ticket_id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('service.service_id'))



Session = sessionmaker(db)
create_session = Session()

Base.metadata.create_all(db)


# Create the class tables

#Table for Salesperson
sales1 = Salesperson(sales_person_id="1",sales_person_name="Venus")
create_session.add(sales1)
create_session.commit()

#Table for Car
car1 = Car(car_id="1",customer_id="Venus",sales_person_id = "1",service_id="1")
create_session.add(car1)
create_session.commit()

#Table Customer
Cus1 = Customer(customer_id="1",customer_name="Juice")
create_session.add(Cus1)
create_session.commit()

#Table for Mechanics
mec1 = Mechanics(mechanic_id="1",mechanic_name="Jose")
create_session.add(mec1)
create_session.commit()

#Table for Payment
Pay1 = Payment(payment_id="1",inventory_id="Venus",customer_id="1",sales_person_id="5")
create_session.add(Pay1)
create_session.commit()

#Table for Inventory
Inv1 = Inventory(inventory_id="1",fee="20")
create_session.add(Inv1)
create_session.commit()

#Table for Parts
Part1 = Parts(parts_id="1",address_id="10")
create_session.add(Part1)
create_session.commit()

#Table for Service
Serve1 = Service(service_id="1",mechanic_id="Venus",parts_id="3")
create_session.add(Serve1)
create_session.commit()

#Table for Servicehistory
servicehist = Servicehistory(service_history_id="1",car_id="1",payment_id="2")
create_session.add(servicehist)
create_session.commit()

#Table for Serviceticket
Servetick = Salesperson(service_ticket_id="1",service_id="Venus")
create_session.add(Servetick)
create_session.commit()