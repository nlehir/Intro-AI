import ipdb
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def function_to_minimize(x, y):
    return x**3 + x**4 + y**4 + 4 * y ** 2 + 5 - x


def xgradient(x, y):
    return 3 * x**2 +4*x**3- 1


def ygradient(x, y):
    return 4 * y**3 + 8 * y

# plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
S = X + Y

for i in range(S.shape[0]):
    for j in range(S.shape[1]):
        S[i][j] = function_to_minimize(X[i][j], Y[i][j])

ax.plot_wireframe(X, Y, S, rstride=5, cstride=10)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('function_to_minimize.pdf')
plt.close()

# initialize the starting point
scope = 4
x_star = np.random.uniform(-scope, scope)
y_star = np.random.uniform(-scope, scope)


# iterate the gradient algorithm
N_iterations = 1000
alpha = 0.01
for iteration in range(N_iterations):
    x_gradient_vector = xgradient(x_star, y_star)
    y_gradient_vector = ygradient(x_star, y_star)
    x_star = x_star - alpha * x_gradient_vector
    y_star = y_star - alpha * y_gradient_vector
    z = function_to_minimize(x_star, y_star)
    print(x_star, y_star, z)
