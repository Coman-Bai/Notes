"""
import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0.0001, 10, 0.1)
y = np.log(x)
print(y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x) = ln x')
plt.scatter([1], [0], c='r')
ax = plt.gca()
plt.plot(x,y)
plt.plot([0, 10], [0, 0], c='b', linestyle='--')
plt.plot([1, 1], [-5, 5], c='b', linestyle='--')
plt.show()
"""

import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(-3, 3, 0.1)
y = x*x
#z = np.array(x)
#a = np.array(1+x+0.5*x*x)
#b = np.array(a+ 0.167*x*x*x)
plt.xlabel('x')
plt.ylabel('E')
plt.title('Elasticity Potential Energy')
#plt.scatter([0], [1], c='r')
#ax = plt.gca()
plt.plot(x, y, color = 'red')
#plt.plot(x, z, color = 'yellow')
#plt.plot(x, a, color = 'black')
#plt.plot(x, b, color = 'pink')
#plt.plot([-2, 2], [4, 4], c='b', linestyle='--')
#plt.plot([-2, -2], [0, 4], c='b', linestyle='--')
#plt.plot([2, 2], [0, 4], c='b', linestyle='--')
plt.show()
