import ipdb
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math


def function_to_minimize(x, y):
    return 0.5*y+0.1*(x**2+y**2)\
        - 100*math.exp(-((x-11.5)**2+(y-8.2)**2)/5)\
        - 200*math.exp(-((x+9)**2+(y+11)**2)/10)


def xgradient(x, y):
    return 0.2*x +\
        100*math.exp(-((x-11.5)**2+(y-8.2)**2)/5)*(2/5)*(x-11.5) +\
        200*math.exp(-((x+9)**2+(y+11)**2)/10)*(2/10)*(x+9)


def ygradient(x, y):
    return 0.5+0.2*y +\
        100*math.exp(-((x-11.5)**2+(y-8.2)**2)/5)*(2/5)*(y-8.2) +\
        200*math.exp(-((x+9)**2+(y+11)**2)/10)*(2/10)*(y+11)


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
plt.savefig('function_to_minimize_2.pdf')
plt.close()

# initialize the starting point
scope = 100

x_star = np.random.uniform(-scope, scope)
y_star = np.random.uniform(-scope, scope)

# iterate the gradient algorithm
N_iterations = 100000
alpha = 0.001
for iteration in range(N_iterations):
    x_gradient_vector = xgradient(x_star, y_star)
    y_gradient_vector = ygradient(x_star, y_star)
    x_star = x_star - alpha*x_gradient_vector
    y_star = y_star - alpha*y_gradient_vector
    # print(x_gradient_vector)
    z = function_to_minimize(x_star, y_star)
    if iteration % 50 == 0:
        print(f"\niteration {iteration}")
        print(f"x* : {x_star:.2f} y* : {y_star:.2f}  value : {z:.2f}")
