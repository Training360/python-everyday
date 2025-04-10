import numpy as np
import matplotlib.pyplot as plt

# Generate data for the normal distribution
mean = 0
std = 1
data = np.random.normal(mean, std, 1000)

# Plot the histogram of the data
plt.hist(data, bins=25, density=True)

# Add a line showing the expected normal distribution
# x = np.linspace(-3, 3, 100)
# y = 1 / (np.sqrt(2 * np.pi) * std) * np.exp(-(x - mean) ** 2 / (2 * std ** 2))
# plt.plot(x, y)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Normal Distribution')

# Show the plot
plt.show()
