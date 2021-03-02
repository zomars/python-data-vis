import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 256, 3125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=3)

# Set chart title and label axes.
ax.set_title("Cube Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
