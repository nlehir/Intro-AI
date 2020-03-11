import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

# load the data
data_1 = np.load("data/ex2/data_1.npy")
data_2 = np.load("data/ex2/data_2.npy")
data = np.concatenate((data_1, data_2))
class_1 = np.zeros(data_1.shape[0])
class_2 = np.ones(data_2.shape[0])
classes = np.concatenate((class_1, class_2))

# split the set into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    data, classes, test_size=0.33, random_state=42)

# fit the model
# clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=500)
clf = SGDClassifier()
clf.fit(X_train, y_train)

nb_test_points = X_test.shape[0]
test_classes = np.zeros(nb_test_points)
for index in range(nb_test_points):
    test_point = X_test[index]
    predicted_class = clf.predict([test_point])
    test_classes[index] = predicted_class

# test the predictor on the test set
plt.scatter(X_test[:, 0],
            X_test[:, 1],
            c=test_classes,
            cmap=plt.cm.Paired,
            edgecolor='black', s=20)

plt.axis('tight')
plt.savefig("images/ex2/prediction_test_set.pdf")
plt.title("Prediction on test set")
plt.close()
