import numpy as np
from sklearn.cluster import KMeans

mean_1 = (600, 2)
std_1 = 90

mean_2 = (200, 100)
std_2 = 50

mean_3 = (-400, 100)
std_3 = 100

n_cluster = 2000
# GENERATE THE DATA
data_1 = np.random.normal(loc=mean_1, scale=std_1, size=(n_cluster, 2))
data_2 = np.random.normal(loc=mean_2, scale=std_2, size=(n_cluster, 2))
data_3 = np.random.normal(loc=mean_3, scale=std_3, size=(n_cluster, 2))
data = np.concatenate((data_1, data_2))
data = np.concatenate((data, data_3))

kmeans = KMeans(n_clusters=3, random_state=0).fit(data)
kmeans.labels_

print(kmeans.predict([[230, 105], [-500, 200]]))

kmeans.cluster_centers_
