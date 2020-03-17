import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

x_values_1 = list(range(1, 1001))
y_values_1 = [x**2 for x in x_values_1]
# plt.scatter(x_values_1, y_values_1, c='red', edgecolor='none', s=40)

plt.scatter(x_values_1, y_values_1, c=y_values_1, cmap=plt.cm.Blues, edgecolor='none', s=40)
# Set the chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('square.png', bbox_inches='tight')
plt.show()
