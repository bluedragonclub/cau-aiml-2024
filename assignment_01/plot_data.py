import numpy as np
import matplotlib.pyplot as plt

from regression import func


# Load the data.
data = np.loadtxt("train_data.csv",
                  delimiter=",",
                  skiprows=1)

x = data[:, 0]
y = data[:, 1]

# Predict the y-values with my function.
y_hat = func(x)

# Calculate the mean squared error (MSE).
mse = np.mean((y - y_hat)**2)

print("MSE:", mse)


# Plot the data.
fig = plt.figure()
plt.scatter(x, y)

plt.xlabel("x", labelpad=8, fontsize=28)
plt.ylabel("y", labelpad=8, fontsize=28)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)


fig.set_size_inches(9.6, 7.2)
fig.tight_layout()
fig.savefig("scatter.jpg", dpi=300)

