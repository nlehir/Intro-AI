import matplotlib.pyplot as plt
import numpy as np
import math


def relufunc(x):
    return max(0, x)


x_data = np.arange(-5, 5, 0.1)
y_data = [relufunc(x) for x in x_data]
plt.plot(x_data, y_data, label="relu\n"+r"$Relu(x)=max(0,x)$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("relu_zoom_in.pdf")
plt.close()


x_data = np.arange(-15, 15, 0.1)
y_data = [relufunc(x) for x in x_data]
plt.plot(x_data, y_data, label="relu\n"+r"$Relu(x)=max(0,x)$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("relu.pdf")
plt.close()


# zoom out
x_data = np.arange(-100, 100, 0.5)
y_data = [relufunc(x) for x in x_data]

plt.plot(x_data, y_data, label="relu\n"+r"$Relu(x)=max(0,x)$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("relu_zoom_out.pdf")
plt.close()
