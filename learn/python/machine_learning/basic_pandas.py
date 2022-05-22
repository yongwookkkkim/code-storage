import pandas as pd
data1=['a', 'b', 'c', 'd', 'e']
sr1=pd.Series(data1)
#print(sr1)
#print(sr1.loc[0])
#print(sr1.loc[1:4]) #both lower and upper bounds inclusive

data2=[1.00, 2.00, 3.14, 100.00, -10.00]
sr2=pd.Series(data2)
#print(sr2)

dict_data={'c0':sr1, 'c1':sr2}
df1=pd.DataFrame(dict_data)
#print(df1)

df1.columns=['string', 'number']
df1.index=['r0', 'r1', 'r2', 'r3', 'r4']
print(df1.loc['r0':'r3', 'string':'number'])