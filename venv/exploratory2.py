import pandas as pd
import psycopg2
from psycopg2 import Error
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import numpy as np
colors=['b', 'r', 'g', 'm', 'y']
def histograms(df):
    fig=plt.figure(figsize=(12,12))
    ax2=fig.add_subplot(2,1,2)
    i=1
    for column in df.columns:
        ax1=fig.add_subplot(3,len(df.columns),i)
        ax1.grid(True)
        n=1+int(math.log2(len(df[column])))
        df[column].hist(bins=n,edgecolor='black',ax=ax1,color=colors[i-1])
        df[column].plot.kde(ax=ax2, linewidth=2, color=colors[i-1], bw_method=(df[column].max()-df[column].min())/n)
        ax1.set_title(column)
        i+=1
    ax2.grid(True)
    ax2.legend()
    ax2.set_ylim(0)
    plt.show()
def characterization(df):
    print(df.describe())
    print(df.corr())

def boxes(df):
    fig,ax1=plt.subplots(figsize=(10,10))
    df.boxplot(ax=ax1)
    plt.show()
def scattering_diagram(df,feature):
    fig=plt.figure(figsize=(10,10))
    ax=fig.add_subplot(111)
    for column in df.columns.tolist():
        if column!=feature:
            ax.scatter(df[column],df[feature],label=column)
    ax.legend()
    ax.set_ylabel(feature)
    ax.grid(True)
    X=np.array(df['feature_2']).reshape(-1,1)
    Y=np.array(df['feature_4']).reshape(-1,1)
    reg=LinearRegression().fit(X,Y)
    a=reg.coef_[0][0]
    b=reg.intercept_[0]
    x=np.linspace(df['feature_2'].min(),df['feature_2'].max(),1000)
    ax.plot(x,a*x+b,color='orange')
    plt.show()
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="readonly",
                                  # пароль, который указали при установке PostgreSQL
                                  password="6hajV34RTQfmxhS",
                                  host="dsstudents.skillbox.ru",
                                  port="5432",
                                  database="db_ds_students")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT * from exploratory;")
    # Получить результат
    record = cursor.fetchall()
    df=pd.DataFrame(record,columns=['feature_{}'.format(i) for i in range(1,6)])
    df=df.astype(float)
    #df['feature_3']=df[df['feature_3']<30]['feature_3']
    characterization(df)
    histograms(df)
    boxes(df)
    scattering_diagram(df,'feature_4')
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

