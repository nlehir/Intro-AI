"""
Create data to study overfitting
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

file_name = 'noisy_data.csv'

inputs = np.random.uniform(-100, 100, 100)
# print(x)
# create data with random noise
outputs = [(0.2*(x-40))**3+(x-40)**2 + 500 * np.random.rand() for x in inputs]


with open(file_name, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for point in range(len(inputs)):
        filewriter.writerow([inputs[point], outputs[point]])


title = 'Noisy data'
file = 'data_to_fit.pdf'
plt.plot(inputs, outputs, 'o')
plt.xlabel('input')
plt.ylabel('output')
plt.title(title)
plt.savefig('images/' + file)
