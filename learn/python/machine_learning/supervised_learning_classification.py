import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

iris=datasets.load_iris()

df=pd.DataFrame(iris['data'], columns=iris['feature_names'])
df.columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df['target']=iris['target']
# df.describe() gives you the statistical info about each column
#print(df.isnull().sum()) # the sum of missing values in each column
#print(df.duplicated().sum()) #duplicated data
#print(df.loc[df.duplicated(),:])
df=df.drop_duplicates()
#print(df.corr()) #the correlation between variables

#a heatmap about correlations
#sns.set(font_scale=1.2)
#sns.heatmap(data=df.corr(), square=True, annot=True, cbar=True)
#plt.show()

#a histogram on sepal length 
#plt.hist(x='sepal_length', data=df)
#plt.show()

#histogram using seaborn.displot
#sns.displot(x='sepal_width', kind='hist', data=df)
#plt.show()

#kde density function using seaborn.displot
#sns.displot(x='petal_width', kind='kde', data=df)
#plt.show()

#for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
#    sns.displot(x=col, hue='target', kind='kde', data=df)
#plt.show()

#sns.pairplot(df, hue='target', size=2.5, diag_kind='kde')
#plt.show()

