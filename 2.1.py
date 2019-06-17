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

plt.figure('Populasi Negara ASEAN',figsize=(10,8))
plt.bar(sea['Name'], sea['Population'], color = warna)
plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa)')
plt.xticks(rotation=45)
plt.grid()

for penduduk in range(len(sea)):
    plt.text(sea['Name'][penduduk], sea['Population'][penduduk] + 1000000, sea['Population'][penduduk])

plt.show()