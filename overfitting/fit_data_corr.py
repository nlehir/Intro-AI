"""
fit the noisy data
"""

import matplotlib.pyplot as plt
import csv
import ipdb
import numpy as np
import random

# open file
file_name = 'linear_noisy_data.csv'

inputs = []
outputs = []

with open(file_name, 'r') as f:
    reader = csv.reader(f)
    # read file row by row
    # convert to lists
    row_index = 0
    for row in reader:
        # print(row)
        if row_index >= 1:
            inputs.append(float(row[0]))
            outputs.append(float(row[1]))
        row_index = row_index + 1

# print(inputs)
# print(outputs)

"""
select training set
"""

nb_points = len(inputs)
nb_training_points = int(0.7 * nb_points)
training_indexes = random.sample(range(nb_points), nb_training_points)
test_indexes = [index for index in range(nb_points)
                if index not in training_indexes]
# print(training_indexes)
# print(test_indexes)

# ipdb.set_trace()

x_train = [inputs[i] for i in training_indexes]
y_train = [outputs[i] for i in training_indexes]
x_test = [inputs[i] for i in test_indexes]
y_test = [outputs[i] for i in test_indexes]


def fit_polynom(degree, x_train, y_train):
    return np.polyfit(x_train, y_train, degree)


def compute_test_error(polynom, x_test, y_test):
    errors = np.polyval(polynom, x_test) - y_test
    square_errors = [error**2 for error in errors]
    total_error = sum(square_errors)
    return total_error


# def plot_polynom_training(polynom, x_train, y_train):
#     degree = len(polynom)
#     title = 'Polynomial fit on training set, degree=' + str(degree)
#     file = 'Fit_degree_' + str(degree) + '.pdf'
#     x_plot = np.linspace(-50, 50, 500)
#     plt.plot(x_train, y_train, 'o', x_plot, np.polyval(polynom, x_plot), '-')
#     # plt.plot(x_train, np.polyval(polynom, x_train), '-')
#     plt.xlabel('training inputs')
#     plt.ylabel('training outputs')
#     plt.xlim(-50, 50)
#     plt.ylim(-200, 200)
#     plt.title(title)
#     plt.savefig('images/' + file)
#     plt.close()


def plot_polynom_sample(polynom, x_train, y_train):
    degree = len(polynom)
    title = 'Polynomial fit on training set, degree=' + str(degree)
    file = 'Fit_degree_' + str(degree) + '.pdf'
    x_plot = np.linspace(-50, 50, 500)
    plt.plot(x_train,
             y_train,
             'o',
             x_test,
             y_test,
             'x',
             x_plot,
             np.polyval(polynom, x_plot), '-')
    plt.legend(['training set', 'test set', 'model'], loc='best')
    # plt.plot(x_train, np.polyval(polynom, x_train), '-')
    plt.xlabel('training inputs')
    plt.ylabel('training outputs')
    plt.xlim(-50, 50)
    plt.ylim(-250, 250)
    plt.title(title)
    plt.savefig('images/' + file)
    plt.close()


def plot_polynom_zoom_out(polynom, x_train, y_train):
    degree = len(polynom)
    title = 'Polynom prediction on global dataset, degree=' + str(degree)
    file = 'Global_degree_' + str(degree) + '.pdf'
    x_plot = np.linspace(-100, 100, 500)
    plt.plot(inputs, outputs, 'o', x_plot, np.polyval(polynom, x_plot), '-')
    # plt.plot(inputs, np.polyval(polynom, inputs))
    plt.xlabel('global inputs')
    plt.ylabel('global outputs')
    plt.xlim(-100, 100)
    plt.ylim(-1000, 1000)
    plt.title(title)
    plt.savefig('images/' + file)
    plt.close()


for degree in range(30):
    print('degree ' + str(degree))
    poly = fit_polynom(degree, x_train, y_train)
    print(compute_test_error(poly, x_test, y_test))
    plot_polynom_sample(poly, x_train, y_train)
    plot_polynom_zoom_out(poly, x_train, y_train)
