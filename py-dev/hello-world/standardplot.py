"""module docstring."""
import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np

X = np.linspace(0, 20, 100)
plt.plot(X, np.sin(X))
plt.show()
