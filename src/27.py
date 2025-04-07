import numpy as np
import matplotlib.pyplot as plt

# Generating some data
x = np.linspace(0, 10, 100)
y = x * np.sin(x)

# Plotting the data
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x) + y')
plt.title('Graph of sin(x) with y = x*sin(x)')
plt.legend()
plt.show()
