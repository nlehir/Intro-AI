import matplotlib.pyplot as plt
import numpy as np
import math


x_data = np.arange(-5, 5, 0.1)
y_data = [1/(1+math.exp(-x)) for x in x_data]
plt.plot(x_data, y_data, label="sigmoid\n"+r"$\sigma(x)=1/(1+e^{-x})$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("sigmoid_zoom_in.pdf")
plt.close()


x_data = np.arange(-15, 15, 0.1)
y_data = [1/(1+math.exp(-x)) for x in x_data]
plt.plot(x_data, y_data, label="sigmoid\n"+r"$\sigma(x)=1/(1+e^{-x})$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("sigmoid.pdf")
plt.close()


# zoom out
x_data = np.arange(-100, 100, 0.5)
y_data = [1/(1+math.exp(-x)) for x in x_data]

plt.plot(x_data, y_data, label="sigmoid\n"+r"$\sigma(x)=1/(1+e^{-x})$")
plt.legend(loc="best")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.savefig("sigmoid_zoom_out.pdf")
plt.close()
