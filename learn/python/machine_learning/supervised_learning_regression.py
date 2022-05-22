import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

x=[-3,31,-11,4,0,22,-2,-5,-25,-14]
y=[-2,32,-10,5,1,23,-1,-4,-24,-13]

df=pd.DataFrame({'X':x, "Y":y})
#print(df.head()) #the first five rows of the dataframe
#print(df.tail()) # the last five rows of the dataframe

train_features=['X']
target_cols=['Y']

x_train=df.loc[:,train_features]
y_train=df.loc[:,target_cols]

lr=LinearRegression()
lr.fit(x_train, y_train)
#print(lr.coef_[0][0]) # sine the input data is 2D, the coefficient is also 2D
#print(lr.intercept_[0])

#prediction
X_new=np.array(11).reshape(1,1)
print(lr.predict(X_new))