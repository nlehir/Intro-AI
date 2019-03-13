import matplotlib.pyplot as plt
import ipdb
import numpy as np

# load the data
data_1 = np.load("data_1.npy")
data_2 = np.load("data_2.npy")
data = np.concatenate((data_1, data_2))


def straight_line(a, b, x):
    return a*x+b


x_data_1 = data_1[:, 0]
y_data_1 = data_1[:, 1]
x_data_2 = data_2[:, 0]
y_data_2 = data_2[:, 1]
x_data = data[:, 0]
y_data = data[:, 1]

xlim_left = min(x_data)
xlim_right = max(x_data)
ylim_top = max(y_data)
ylim_bottom = min(y_data)


def test_linear_separator(a, b, data):
    print("testing separator with a={} and b={}".format(a, b))
    x_plot = np.linspace(xlim_left, xlim_right, data.shape[0])
    y_plot = [straight_line(a, b, x) for x in x_plot]

    # compute the margin
    separator = np.zeros((data.shape[0], 2))
    separator[:, 0] = x_plot
    separator[:, 1] = y_plot
    distances = []
    # compute the distance between each point in the
    # separator and the dataset
    for point in separator:
        # repeat the point to use linalg.norm
        point_repeated = np.tile(point, (data.shape[0], 1))
        # distances between this point and the dataset
        point_distances = np.linalg.norm(point_repeated-data, axis=1)
        # take the minimum
        point_distance_to_dataset = min(point_distances)
        # store this distance
        distances.append(point_distance_to_dataset)
    # the margin is the maximum of these distances
    margin = min(distances)
    print("margin: {0:.2f}".format(margin))

    plt.plot(x_data_1,
             y_data_1,
             'o',
             color="sandybrown")
    plt.plot(x_data_2,
             y_data_2,
             'o',
             color="darkorchid")
    plt.plot(x_plot,
             y_plot,
             '-',
             color="green")

    plt.xlim(xlim_left-60, xlim_right+60)
    plt.ylim(ylim_bottom-60, ylim_top+60)
    plt.title("linear separation\nmargin: {0:.2f}".format(margin))
    figname = "linear_separator_a={}_b={}".format(a, b)
    plt.savefig("images/"+figname+".pdf")
    plt.close()


test_linear_separator(1, 1, data)
test_linear_separator(2, -1, data)
test_linear_separator(7, -4000, data)
