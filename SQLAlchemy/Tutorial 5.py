from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///mydatabase.db', echo=True)

df = pd.read_sql('Select * from people', con=engine)

print(df)

new_data = pd.DataFrame({'name': ['Ayesha', 'Shivani'], 'age': [26, 24]})

# if_exists, if table already exist, we just add new our data to that table.
new_data.to_sql('people', con=engine, if_exists='append', index=False)