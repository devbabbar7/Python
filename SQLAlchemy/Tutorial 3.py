from sqlalchemy import create_engine, MetaData, text, Table, Column, Integer, String, Float, ForeignKey, func

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    'people', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('age', Integer)
)

things = Table(
    'things', meta,
    Column('id', Integer, primary_key=True),
    Column('description', String(255), nullable=False),
    Column('price', Float),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()

conn.execute(text('Delete from people'))
conn.execute(text('Delete from things'))

insert_people = people.insert().values([
    {'name':'Dev', 'age':24},
    {'name':'John', 'age':25},
    {'name':'Jane', 'age':23}
])

insert_things = things.insert().values([
    {'description':'Laptop', 'price':120000, 'owner':1},
    {'description':'Mobile', 'price':20000, 'owner':1},
    {'description':'Mobile', 'price':20000, 'owner':2}
])

conn.execute(insert_people)
conn.execute(insert_things)
conn.commit()

join_statement = people.outerjoin(things, people.c.id == things.c.owner) # Left outer join
#join_statement = people.join(things, people.c.id == things.c.owner) # Inner join
#join_statement = things.outerjoin(people, people.c.id == things.c.owner) # Right outer join (just reverse order)
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)
result = conn.execute(select_statement)
for row in result:
    print(row)

'''
Output:
('Dev', 'Laptop')
('Dev', 'Mobile')
('John', 'Mobile')
('Jane', None)
'''

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.price), func.avg(things.c.price), func.min(things.c.price), func.max(things.c.price), func.count(things.c.price), func.group_concat(things.c.description)).group_by(things.c.owner).having(func.sum(things.c.price) > 5000)
result = conn.execute(group_by_statement)
for row in result:
    print(row)

'''
Output:
(1, 140000.0, 70000.0, 20000.0, 120000.0, 2, 'Laptop,Mobile')
(2, 20000.0, 20000.0, 20000.0, 20000.0, 1, 'Mobile')    
'''