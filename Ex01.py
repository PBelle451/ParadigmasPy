import math

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-math.pi, math.pi, 0.01)
sin = np.sin(x)
p1 = x
p3 = (x - x**3)/6
p5 = p3 + x**5/120
plt.plot(x, p1, 'm')
plt.plot(x, p3, 'k')
plt.plot(x, p5, 'c')
plt.plot(x, sin)
plt.legend(['seno', 'spaghetti', 'penne', 'ravioli'])
plt.xlabel("x")
plt.ylabel("y")
plt.axis([-math.pi, math.pi, -5, 5])

plt.show()