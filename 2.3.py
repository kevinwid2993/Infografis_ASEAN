import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy

mydb = sqlalchemy.create_engine(
    'mysql+pymysql://kevin:kevin29101993!@localhost:3306/world'
)

df = pd.read_sql('SELECT * FROM country', mydb)
sea = df[df['Region'] == 'Southeast Asia'].reset_index()

warna = ['black', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', '#c2dd3b', '#08fff8', '#1371b6']

plt.figure('Pendapatan Bruto Nasional Asean',figsize=(10,8))
plt.bar(sea['Name'], sea['GNP'], color = warna)
plt.title('Pendapatan Bruto Nasional Asean')
plt.xlabel('Negara')
plt.ylabel('Gross National Product(US$)')
plt.xticks(rotation=45)
plt.grid()

for gnp in range(len(sea)):
    plt.text(sea['Name'][gnp], sea['GNP'][gnp] + 1000, sea['GNP'][gnp])

plt.show()