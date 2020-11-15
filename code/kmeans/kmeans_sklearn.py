import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# load the data
data = np.load("data.npy")

# use sklearn in order to perform the algorithm
kmeans = KMeans(n_clusters=6).fit(data)

# use the learned estimator in order to predict the cluster of a new point
print(kmeans.predict([[230, 105], [-500, 200]]))

# plot the data and the found centroids
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, 'o')
centroids = kmeans.cluster_centers_
x_centroids = list(centroids[:, 0])
y_centroids = list(centroids[:, 1])
plt.plot(x_centroids,
         y_centroids,
         "x",
         color="orange",
         label="centroids")
plt.legend(loc="best")
plt.savefig('sklearn_centroids.pdf')
plt.close()
