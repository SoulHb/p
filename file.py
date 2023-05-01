import numpy as np
from matplotlib import pyplot as plt

def one():
	a = np.zeros((100,100))
	a[10,10]=1
	return a

a = one()
plt.imshow(a)
plt.show()
