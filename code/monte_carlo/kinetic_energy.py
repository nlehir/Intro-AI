import numpy as np
import matplotlib.pyplot as plt
import math

mass = 2e-26
electron_volt = 1.602e-19


def approximate(N):
    estimator = 0
    for i in range(N):
        estimator += np.random.uniform(0, 1000)**2
    estimator = estimator * mass/2
    return estimator/N


real_value = mass/2 * (1000**3)/3/1000
print(real_value)

min_samples = 100
max_samples = int(4e5)
nb_tests = 60
step = int((max_samples-min_samples)/nb_tests)
inputs = range(min_samples, max_samples, step)
approx = []
for N in inputs:
    approximation = approximate(N)
    print(f"estimation for N={N} : I={approximation}")
    error = abs(approximation-real_value)
    error_in_eV = error / electron_volt
    approx.append(error_in_eV)


plt.plot(inputs, approx, "o")
plt.xlabel('Number of samples')
plt.ylabel('Error (eV)')
plt.title("Monte Carlo error as a function \nof the number of samples")
plt.savefig(f"images/error_linear.pdf")
plt.close()

sq_inputs = [x**(1/2) for x in inputs]
plt.plot(sq_inputs, approx, "o")
plt.xlabel('Square root of number of samples')
plt.ylabel('Error (eV)')
plt.title(
    "Monte Carlo error as a function \nof the square root of\n the number of samples")
plt.savefig(f"images/error_square_root.pdf")
plt.close()
