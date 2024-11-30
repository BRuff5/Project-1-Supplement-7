import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to plot 200 points.
def plot_normal_distribution():
    data = np.random.randn(200)
    # Create a grapgh of the data
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, alpha=0.7, color='blue')
    plt.title('Graph 200 Points from Standard Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

    """
    Plot 200 points sampled from a standard normal distribution.
    Args:
        None
    Returns:
        Graph
    """
    
# Function to plot a line given the y-intercept, the slope, the lower x boundary, and the upper x boundary.
def plot_line(y_intercept, slope, lower_x, upper_x):
    """
    Plot a line defined by a y-intercept and slope within specified x boundaries.

    Args:
        y_intercept (float): The y-intercept of the line.
        slope (float): The slope of the line.
        lower_x (float): The lower bound of the x-axis.
        upper_x (float): The upper bound of the x-axis.

    Returns:
        Graph
    """
    # Generate x values
    x_values = np.linspace(lower_x, upper_x, 100)
    # Calculate y values y = mx + b
    y_values = slope * x_values + y_intercept

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, color='red', label=f"y = {slope}x + {y_intercept}")
    plt.title('Line Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(lower_x * slope + y_intercept - 10, upper_x * slope + y_intercept + 10)  
    plt.xlim(lower_x, upper_x)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid()
    plt.legend()
    plt.show()

