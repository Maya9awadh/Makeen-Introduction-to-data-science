# -*- coding: utf-8 -*-
"""
read dataset, summarize it, and do some visualization on
it
"""
#imported library
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#read csv file
df=pd.read_csv('Dry Beans Dataset.csv')
print(df.head)

#Count and distribution of all beans categories
print(df['Class'].value_counts())
_ = sns.countplot(x='Class', data=df)
Numeric_cols = df.drop(columns=['Class']).columns

fig, ax = plt.subplots(8, 2, figsize=(15, 25))
for variable, subplot in zip(Numeric_cols, ax.flatten()):
    sns.boxplot(x=df['Class'], y= df[variable], ax=subplot)
plt.tight_layout()
#describe the data
print(df.describe())

