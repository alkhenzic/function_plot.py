import matplotlib.pyplot as plt
import numpy as np

def plot_function(function, start, end):
    """Строит график заданной функции на заданном интервале."""
    x = np.linspace(start, end, 100)
    y = function(x)
    plt.plot(x, y)
    plt.xlabel
