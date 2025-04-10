import numpy as np
from matplotlib import pyplot as plt
from snippets import ages_x, dev_y, py_dev_y, js_dev_y

# bar - overlaping by default
# np.arange
# replace ages_x to x_indexes
# width
# xticks

width = 0.25
plt.style.use('seaborn-v0_8-bright')
x_indexes = np.arange(len(ages_x))
plt.bar(x_indexes, py_dev_y, width=width, color='#0000FF',  label="Python devs")
plt.bar(x_indexes + width, js_dev_y, width=width, color='#FFFF00', label="JS devs")
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title("Median Salary (USD) by age")
plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.grid(True)
plt.tight_layout()
plt.savefig('plot.svg')
plt.show()
