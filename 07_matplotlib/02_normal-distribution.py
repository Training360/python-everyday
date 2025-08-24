import numpy as np
import matplotlib.pyplot as plt

# Generate data for the normal distribution
mean = 0
std = 1
data = np.random.normal(mean, std, 1000)

# Plot the histogram of the data
# data: Az adatokat tartalmazó tömb (itt 1000 véletlenszerűen generált szám normál eloszlással)

# bins=25:

# A hisztogramot 25 "vödörre" (bin) osztja
# Minden vödör egy értéktartományt képvisel
# Minél több a vödör, annál részletesebb a hisztogram
# density=True:

# A hisztogram Y tengelyét normalizálja, hogy a görbe alatti terület összege 1 legyen
# Ezzel valószínűségi sűrűségfüggvényként (PDF) ábrázolja a hisztogramot
# Így közvetlenül összehasonlítható az elméleti normál eloszlás görbéjével
# density=False esetén a nyers gyakoriságokat mutatná
plt.hist(data, bins=25, density=True)

# Add a line showing the expected normal distribution
# x = np.linspace(-3, 3, 100)
# y = 1 / (np.sqrt(2 * np.pi) * std) * np.exp(-(x - mean) ** 2 / (2 * std ** 2))
# plt.plot(x, y)

# Add labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Normal Distribution")

# Show the plot
plt.show()
