import matplotlib.pyplot as plt

square_value = [1, 4, 9, 16, 25]
square = [1, 2, 3, 4, 5]
# Below gives incorrect graph as the plot will start graph from 0 not one
# plt.plot(squares, linewidth=5)
# Below gives us accurate as we give both input and output
plt.plot(square, square_value, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
