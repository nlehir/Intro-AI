"""
Create data to study overfitting
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

file_name = 'linear_noisy_data.csv'

inputs = np.random.uniform(-40, 40, 50)
# print(x)
# create linear data with random noise
outputs = [4.5 * x + 60 * np.random.rand() for x in inputs]


with open(file_name, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for point in range(len(inputs)):
        filewriter.writerow([inputs[point], outputs[point]])


title = 'Noisy data'
file = 'noisy_data.pdf'
plt.plot(inputs, outputs, 'o')
plt.xlabel('input')
plt.ylabel('output')
plt.title(title)
plt.savefig('images/' + file)
