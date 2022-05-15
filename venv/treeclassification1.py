import isin as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

data_train=pd.read_csv('1.8_phones.csv')
print(data_train)
data_train['os']=data_train['os'].apply(lambda x:1 if x=='Android' else 0)
print(data_train)
features=data_train[['disk','price','os']]
label=data_train['year']
clf=DecisionTreeClassifier().fit(features,label)

x_test=pd.DataFrame([[22,100,0]],columns=['disk','price','os'])
print(x_test)
label_predict=clf.predict(x_test)[0]
print(tree.export_text(clf))
print(label_predict)
