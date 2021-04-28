import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

### Importing the data set
df = pd.read_csv(r'laundry_data.csv')
print(df.head())

### Identifying the number and data types of features
print(list(df.columns))

df.columns = ['avail', 'avg_runtime', 'datetime', 'id', 'machine_no', 'offline', 'room', 'time_remaining', 'type']
print(df.dtypes)

### Identifying the number of observations
print(len(df))

### Checking if the dataset has empty cells or samples

print(df.isnull().values.any())
print(df.isnull().sum())

print(df[df['machine_no'].isna()])

### Number of unique values
print(len(set(df.avail)) , set(df.avail))

print(len(set(df.avg_runtime)) , set(df.avg_runtime))
print(len(set(df.datetime)) , set(df.datetime))
print(len(set(df.id)) , set(df.id))
print(len(set(df.machine_no)) , set(df.machine_no))
print(len(set(df.offline)) , set(df.offline))
print(len(set(df.room)) , set(df.room))
print(len(set(df.time_remaining)) , set(df.time_remaining))
print(len(set(df.type)) , set(df.type))

### List of dryers and washers in each room

group = df.groupby('room')
df2 = group.apply(lambda x: len(x['id'].unique()))
print(df2)