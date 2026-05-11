from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()

conn.execute(text('Create table if not exists people (name str, age int)'))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)
session.execute(text("Insert into people (name, age) values ('Dev', 24)"))
session.commit()