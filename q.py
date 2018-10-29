import numpy as np
import matplotlib.pyplot as plt

p = np.random.poisson(5, 1000)
plt.hist(p, normed=True)
plt.show()

s = np.random.normal(0, 5, 1000)
plt.hist(s, normed=True)
plt.show()
