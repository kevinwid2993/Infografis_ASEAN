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

plt.figure('Persentase Luas Daratan Asean', figsize=(10,8))
plt.pie(sea['SurfaceArea'],labels=sea['Name'], autopct='%1.1f%%')
plt.title('Persentase Luas Daratan Asean')
plt.show()