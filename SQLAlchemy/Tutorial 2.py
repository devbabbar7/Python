from sqlalchemy import create_engine, MetaData, text, Table, Column, Integer, String, Insert
import urllib.parse
'''
# To connect with mysql
user = 'root'
password = 'root'
password = urllib.parse.quote_plus(password) # if password has special characters
host = 'localhost'
port = 3306
database = 'dbms'

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", echo=True)
'''
engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    'people', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)

conn = engine.connect()
conn.execute(text('delete from people'))

insert_statement = people.insert().values(name='Dev', age=23)
insert_statement2 = Insert(people).values(name='John', age=24)
insert_statement3 = Insert(people).values(name='Temp', age=99)
update_statement = people.update().where(people.c.name == 'John').values(age=25)
delete_statement = people.delete().where(people.c.name == 'Temp')
_ = conn.execute(insert_statement)
_ = conn.execute(insert_statement2)
_ = conn.execute(insert_statement3)
_ = conn.execute(update_statement)
_ = conn.execute(delete_statement)
conn.commit()

select_statement = people.select().where(people.c.age > 22)
result = conn.execute(select_statement)
print(type(result))
for row in result:
    print(row.name, row)

'''
Output:
Dev (1, 'Dev', 23)
John (2, 'John', 25)
'''