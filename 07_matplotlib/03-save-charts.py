from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('seaborn-v0_8-bright')
plt.xkcd()

# plot
# x,y labels
# title
# label, legend
# formatString: https://python-course.eu/numerical-programming/formatting-plot-in-matplotlib.php
# named params instead formatstring
# marker
# hex color
# linewidth
# tight_layout: a plotok közötti eltartást álíltja, kijelzőfüggő is
# style
# xkcd

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, 'k--', label="Python devs")
plt.plot(ages_x, dev_y, color="#000000", linestyle="--",
         marker=".", label="All devs")

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Add a second line
plt.plot(ages_x, py_dev_y, color='#0000FF',
         marker="o", linewidth=3, label="Python devs")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#FFFF00',
         marker="o",  linewidth=3,  label="JS devs")


# Add labels
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title("Median Salary (USD) by age")

# legend, not good, before the order is important
# plt.legend(['All devs', 'Python devs'])

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plot.svg')
plt.show()
