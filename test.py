import matplotlib.pyplot as plt
import numpy as np

m = 17.36
b = 19.503999999999998
x = np.linspace(0, 10, 100)
y = m * x + b

plt.plot(x, y)
plt.xlabel("Training Time (hours)")
plt.ylabel("Accuracy (%)")
plt.title("Linia redresoare")
plt.show()

