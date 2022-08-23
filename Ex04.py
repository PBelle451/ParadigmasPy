import math

import matplotlib.pyplot as plt
import numpy as np
theta = np.arange(0, 2 * math.pi, 0.01)
l=5
e=1
r = l / (e * np.cos(theta) + 1)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.polar(theta, r)
plt.show()
