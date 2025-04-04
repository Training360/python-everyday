import matplotlib.pyplot as plt
import numpy as np
# if using a jupyter notebook

x = np.arange(0, 15, 0.1)   # start,stop,step
print(x)
y = np.sin(x)
plt.plot(x, y)
plt.show()
