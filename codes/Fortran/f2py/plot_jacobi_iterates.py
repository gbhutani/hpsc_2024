
from matplotlib import pyplot as plt
import numpy as np
import time

import jacobi1   # created from jacobi1.f90 using f2py

n = 51

# grid points:
x = np.linspace(0., 1., n)

# boundary conditions:
alpha = 20.
beta = 60.

# initial guess:
u = np.linspace(alpha, beta, n)

# right hand side:
f = 100. * np.exp(x)

niters = 0
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(x, u, 'o-')
ax.set_title("After %s iterations" % niters)
ax.set_ylim([10., 80.])

ans = input("Type return to start... ")

iters_per_plot = 200   # number of iterations between plots
nplots = 20            # number of plots to produce

for nn in range(nplots):
    u = jacobi1.iterate(u, iters_per_plot, f)
    line.set_ydata(u)
    niters = niters + iters_per_plot
    ax.set_title("After %s iterations" % niters)
    plt.draw()
    plt.pause(0.5)  # Pause to allow the plot to update