# -*- coding: utf-8 -*-
"""
In this script a neural network tries to fit randomly generated data
"""
import plot_net
import os
import ipdb
import numpy as np
import matplotlib.pyplot as plt


# HYPERPARAMETERS
hidden_dim = 2
Learning_rate = 1e-6

# Plotting parameters
Nb_steps = 50000
Nb_plotted_steps = 50

# selection of the data
noise_std_dev = 0.0
# load the data
x_train = np.load("data/training_inputs_std_" + str(noise_std_dev) + ".npy")
y_train = np.load("data/training_outputs_std_" + str(noise_std_dev) + ".npy")

x_test = np.load("data/test_inputs_std_" + str(noise_std_dev) + ".npy")
y_test = np.load("data/test_outputs_std_" + str(noise_std_dev) + ".npy")

# ipdb.set_trace()


def fit_structured_data(x_train, y_train, hidden_dim):
    input_dim = x_train.shape[1]
    output_dim = y_train.shape[1]
    figname = (
        "d_in_"
        + str(input_dim)
        + "_d_out_"
        + str(output_dim)
        + "_hidden__"
        + str(hidden_dim)
        + "_std_"
        + str(noise_std_dev)
        + "_rate_"
        + str(Learning_rate)
    )
    # directory where we will store results
    dir_name = "visualization/structured_data/" + figname + "/"

    # ----------------------
    # INITIALIZATION OF THE WEIGHTS
    # Randomly initialize weights
    w1 = np.random.randn(input_dim, hidden_dim)
    w2 = np.random.randn(hidden_dim, output_dim)

    # we will store the loss as a function of the
    # optimization step
    losses = []
    steps = []
    for step in range(Nb_steps):
        # ----------------------
        # FORWARD PASS
        # Prediction of the network for a given input x
        hh = x_train.dot(w1)
        h_relu = np.maximum(hh, 0)
        y_pred = h_relu.dot(w2)

        # ----------------------
        # LOSS FUNCTION
        # Here we use the Square Error loss
        loss = np.square(y_pred - y_train).sum()

        # ----------------------
        # Plot the network and the loss
        if step % (Nb_steps / Nb_plotted_steps) == 0:
            print(step, loss)
            graph_name = "net_" + str(step)

            # keep storing the loss and the steps
            losses.append(loss)
            steps.append(step)

            # Plot the evolution of the loss
            # We will not plot all the points
            scale = 5
            printed_steps = [
                steps[x[0]] for x in enumerate(losses) if x[1] < loss * scale
            ]
            printed_losses = [x for x in losses if x < loss * scale]
            plt.plot(printed_steps, printed_losses, "o")
            # set the limits of the plots to make it nice
            plt.xlim([min(printed_steps) * 0.5, max(printed_steps) * 1.2 + 1])
            plt.ylim([0.2 * min(printed_losses), 1.5 * max(printed_losses)])
            plt.title("Loss function (square error)")
            plt.draw()
            plt.pause(0.01)

            # ----------------------
            # Print the network with gaphviz
            plot_net.show_net(
                step,
                w1,
                w2,
                input_dim,
                hidden_dim,
                output_dim,
                figname,
                dir_name,
                graph_name,
                loss,
                Learning_rate,
            )

        # -----------------------
        # BACKPROPAGATION
        # computation of the gradients of w1 and w2 with respect
        # to the loss function
        # -----------------------
        grad_y_pred = 2.0 * (y_pred - y_train)
        grad_w2 = h_relu.T.dot(grad_y_pred)
        grad_h_relu = grad_y_pred.dot(w2.T)
        grad_h = grad_h_relu.copy()
        grad_h[hh < 0] = 0
        grad_w1 = x_train.T.dot(grad_h)

        # -----------------------
        # UPDATE OF THE WEIGTHS
        # with the results of backpropagation
        w1 -= Learning_rate * grad_w1
        w2 -= Learning_rate * grad_w2

    # -----------------------
    # save the plot of the loss function
    plt.close()
    plt.plot(steps, losses)
    plt.title("Loss function (square error)")
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    plt.savefig(dir_name + "Loss_function.pdf")
    plt.show()
    plt.close("all")
    #print("----")
    #print("error on test set : " + str(predict_on_test_set(x_test, y_test, w1, w2)))


def predict_on_test_set(tested_x, tested_y, w1, w2):
    hh = tested_x.dot(w1)
    h_relu = np.maximum(hh, 0)
    y_pred = h_relu.dot(w2)
    loss = np.square(y_pred - tested_y).sum()
    return loss


if __name__ == "__main__":
    fit_structured_data(x_train, y_train, hidden_dim)
