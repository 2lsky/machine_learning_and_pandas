import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv('1.8_phones.csv')
kmeans = KMeans(n_clusters=3)
X=data[['price','year']]
kmeans.fit(X)
print(kmeans.cluster_centers_)
fig,ax1=plt.subplots(ncols=1,nrows=1,figsize=(10,10))
ax1.scatter(data['price'],data['year'])
ax1.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],cmap='rainbow')
plt.show()

