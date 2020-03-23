import numpy as np
import matplotlib.pyplot as plt


nb_points = int(1e7)
x_data = np.arange(-50, 50, nb_points)
y_data = np.random.normal(20, 25, nb_points)
plt.hist(y_data, bins=100, density=True)
plt.savefig("images/gaussian.pdf")
