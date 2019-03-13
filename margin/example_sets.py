import numpy as np
import matplotlib.pyplot as plt

mean_1 = (600, 2)
std_1 = 70

mean_2 = (180, 130)
std_2 = 80

n_cluster = 200
# GENERATE THE DATA
data_1 = np.random.normal(loc=mean_1, scale=std_1, size=(n_cluster, 2))
data_2 = np.random.normal(loc=mean_2, scale=std_2, size=(n_cluster, 2))
np.save("data_1", data_1)
np.save("data_2", data_2)

plt.plot(data_1[:, 0], data_1[:, 1], 'o', color="sandybrown")
plt.plot(data_2[:, 0], data_2[:, 1], 'o', color="darkorchid")
plt.savefig("data_to_separate.pdf")
plt.close()
