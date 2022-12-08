from aocd.models import Puzzle
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def visualize_input():
    puzzle = Puzzle(year=2022, day=8)
    s = puzzle.input_data
    k = np.array([[int(y) for y in x] for x in s.split("\n") if x])

    x = np.arange(len(k))
    y = np.arange(len(k[0]))
    x, y = np.meshgrid(x, y)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(
        x, y, k, vmin=k.min() * 2, cmap=cm.coolwarm, linewidth=0, antialiased=True
    )
    ax.set_aspect("equal")
    ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

    plt.show()


visualize_input()
