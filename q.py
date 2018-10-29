import numpy as np
import matplotlib.pyplot as plt

p = np.random.poisson(5, 1000)                    #for q1
plt.hist(p, normed=True)
plt.show()



s = np.random.normal(0, 5, 1000)                  #for q2
plt.hist(s, normed=True)
plt.show()


data= []                                          #for q3
for i in range(100):
    r = np.random.randint(0,1000)
    avg = (p[r]+s[r])/2
    data.append(avg)

plt.hist(data,density=True)
plt.show()

