import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 100, 0.01)
y = x
y2 = x**2
y3 = x**3

plt.plot(x, y, 'm')
plt.plot(x, y2, 'c')
plt.plot(x, y3, 'k')
plt.loglog()
plt.legend(['y', 'y2', 'y3'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
