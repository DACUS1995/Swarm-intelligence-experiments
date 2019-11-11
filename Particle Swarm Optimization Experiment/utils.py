import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np

import cost_functions

def plot_function(fn_name):
    function = getattr(cost_functions, f"{fn_name}_fn")

    fig = plt.figure()
    ax = Axes3D(fig)

    # Make data.
    x = np.arange(-5.12, 5.12, 0.05)
    y = np.arange(-5.12, 5.12, 0.05)

    z = [[function([_x, _y]) for _x in np.nditer(x)] for _y in np.nditer(y)]

    X, Y = np.meshgrid(x, y)
    Z = np.array(z)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

if __name__ == "__main__":
    plot_function("griewank")