import pandas as pd
import matplotlib
pd.set_option('display.width', 1000)

df = pd.read_csv('train.csv')

# cleaning
df = df.drop(['Cabin'], axis=1)
df = df.dropna()

male_survivors = df.query("Sex == 'male' & Survived == '1'")

print(male_survivors)