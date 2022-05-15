import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as ticker
def linearregression(file,x,y,z):
    df=pd.read_csv(file)
    reg1=LinearRegression().fit(df[[x]],df[[z]])
    reg2=LinearRegression().fit(df[[y]],df[[z]])
    reg3=LinearRegression().fit(df[[x,y]],df[[z]])

    a1=reg1.coef_[0][0]
    b1=reg1.intercept_[0]
    a2 = reg2.coef_[0][0]
    b2 = reg2.intercept_[0]
    a30=reg3.coef_[0][0]
    a31=reg3.coef_[0][1]
    b3=reg3.intercept_[0]
    f3=lambda x,y:a30*x+a31*y+b3

    fig = plt.figure(figsize=(20,20))
    plt.subplots_adjust(wspace=1)
    ax1=fig.add_subplot(131,projection='3d')
    ax1.set_zlabel('Price')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Disk')
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(3))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(150))
    x1=np.linspace(df[x].min(),df[x].max(),1000)
    y1=np.linspace(df[y].min(),df[y].max(),1000)
    X, Y = np.meshgrid(x1, y1)
    Z=f3(X,Y)
    ax1.plot_surface(X, Y, Z)
    ax1.scatter(df[x],df[y],df[z],color='black')

    ax2 = fig.add_subplot(132)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Price')
    ax2.plot(df[x],a1*df[x]+b1)
    ax2.scatter(df[x],df[z],color='black')

    ax3 = fig.add_subplot(133)
    ax3.set_xlabel('Disk')
    ax3.set_ylabel('Price')
    ax3.plot(df[y], a2 * df[y] + b2)
    ax3.scatter(df[y], df[z], color='black')
    plt.show()
linearregression('1.8_phones.csv','year','disk','price')