from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

iris=datasets.load_iris()
df=pd.DataFrame(iris['data'], columns=iris['feature_names'])

print(type(df))
#knn=KNeighborsClassifier(n_neighbors=7)
#knn.fit(x_train, y_train)