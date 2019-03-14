import numpy as np
import matplotlib.pyplot as plt
import ipdb
from keras.models import model_from_json

y_test = np.load("data/y_test.npy")
x_test = np.load("data/x_test.npy")
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

print("load the model")
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
loaded_model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])


print("evaluate the model")
loss, accuracy = loaded_model.evaluate(x_test, y_test)
print("loss: {}".format(loss))
print("accuracy: {} %".format(100*accuracy))


def predit_test_point(data_index, x_test, y_test):
    nb_test_data = x_test.shape[0]
    if data_index > nb_test_data:
        raise ValueError(
            "data index too large : only {} test samples available".format(nb_test_data))
    print("test data point {}".format(data_index))
    true_label = y_test[data_index]
    # prediction of the model
    pred = loaded_model.predict(x_test[data_index].reshape(1, 28, 28, 1))
    predicted_label = pred.argmax()
    if true_label == predicted_label:
        print("correct prediction: {}".format(predicted_label))
        title = "testing point: {}\ntrue label: {}\npredicted label: {} \nOK".format(
            data_index, true_label, predicted_label)
    else:
        print("wrong prediction: {} instead of {}".format(
            predicted_label, true_label))
        title = "testing point: {}\ntrue label: {}\npredicted label: {}\nMISTAKE".format(
            data_index, true_label, predicted_label)

    # print the result
    plt.imshow(x_test[data_index], cmap="Greys")
    plt.title(title)
    plt.savefig("images/prediction_{}.pdf".format(data_index))
    plt.close()


# predit_test_point(1278, x_test, y_test)
# predit_test_point(178, x_test, y_test)
# predit_test_point(18, x_test, y_test)
# predit_test_point(17, x_test, y_test)
# predit_test_point(278, x_test, y_test)
# predit_test_point(7278, x_test, y_test)
# predit_test_point(9278, x_test, y_test)
# predit_test_point(4275, x_test, y_test)
