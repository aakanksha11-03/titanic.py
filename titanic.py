
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

df = sns.load_dataset('titanic')

print(df.head())

print(df.isnull().sum())

df['age'].fillna(df['age'].median(), inplace=True)

df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

df.drop(columns=['deck'], inplace=True)

sns.boxplot(x=df['fare'])
plt.show()

Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['fare'] >= lower) & (df['fare'] <= upper)]

scaler = StandardScaler()

df[['age', 'fare']] = scaler.fit_transform(df[['age', 'fare']])

df.drop_duplicates(inplace=True)

print(df.info())

print(df.head())