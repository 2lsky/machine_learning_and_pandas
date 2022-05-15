from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import math
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler,StandardScaler
data=load_boston()
boston=pd.DataFrame(data.data,columns=data.feature_names)
Y=data.target
X=pd.DataFrame(np.c_[boston['LSTAT'],boston['RM']],columns=['LSTAT','RM'])
X_train,X_test1,Y_train,Y_test1=train_test_split(X,Y,random_state=42,train_size=0.7)
X_val,X_test,Y_val,Y_test=train_test_split(X_test1,Y_test1,random_state=42,train_size=0.7)
reg=LinearRegression().fit(X_train,Y_train)
Y_predict=reg.predict(X_val)
print('Без трансформации')
print('Стандартное отклонение -',math.sqrt(mean_squared_error(Y_val,Y_predict)))
print('Коэффициент детерминации -',r2_score(Y_val,Y_predict))
reg1=LinearRegression().fit(X_train,np.log(Y_train))
Y_predict1=reg1.predict(X_val)
print('Логарифмирование')
print('Стандартное отклонение -',math.sqrt(mean_squared_error(np.log(Y_val),Y_predict1)))
print('Коэффициент детерминации -',r2_score(np.log(Y_val),Y_predict1))
reg2=LinearRegression().fit(StandardScaler().fit_transform(X_train),Y_train)
Y_predict2=reg2.predict(StandardScaler().fit_transform(X_val))
print('Стандартизация')
print('Стандартное отклонение -',math.sqrt(mean_squared_error(Y_val,Y_predict2)))
print('Коэффициент детерминации -',r2_score(Y_val,Y_predict2))
reg3=LinearRegression().fit(MinMaxScaler().fit_transform(X_train),Y_train)
Y_predict2=reg2.predict(MinMaxScaler().fit_transform(X_val))
print('MinMax')
print('Стандартное отклонение -',math.sqrt(mean_squared_error(Y_val,Y_predict2)))
print('Коэффициент детерминации -',r2_score(Y_val,Y_predict2))


