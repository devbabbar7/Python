from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///mydatabase.db', echo=True)

Base = declarative_base()

class Person(Base): # Name is usually singular
    __tablename__ = 'People' # Table name is plural
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship('Thing', back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    price = Column(Float)
    owner = Column(Integer, ForeignKey('People.id'))

    person = relationship('Person', back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_person = Person(name='John Doe', age=30)
session.add(new_person)
session.flush()

new_thing = Thing(description='Laptop', price=1000.0, owner=new_person.id)
session.add(new_thing)
session.flush()
# You can use flush instead of commit, so the changes will not be saved in the db.
# session.commit()

print([t.description for t in new_person.things])
print(new_thing.person.name)

session.query(Person).filter(Person.name == 'Dev').update({'age': 24})
session.commit() # this will commit previous flushes also.

# John doe will delete because age is 30.
# Notice how we didn't need to commit the change because we added John Doe using flush.
session.query(Person).filter(Person.age>25).delete()
result = session.query(Person).filter(Person.age>20).all()


print([p.name for p in result])

result2 = session.query(Person.name, Thing.description).join(Thing).all()
print(result2)

result3 = session.query(Thing.owner, func.sum(Thing.price)).group_by(Thing.owner).having(func.sum(Thing.price) > 5000).all()
print(result3)

# session.close()

'''
Output:
['Laptop']
John Doe
['Dev', 'John']
[('Dev', 'Laptop'), ('Dev', 'Mobile'), ('John', 'Mobile')]
[(1, 140000.0), (2, 20000.0)]
'''