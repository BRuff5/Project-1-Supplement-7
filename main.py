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
    """Plot a line defined by a y-intercept and slope within specified x boundaries.

    Args:
        y_intercept (float): y-intercept 
        slope (float): slope
        lower_x (float): lower bound 
        upper_x (float): upper bound 
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

# Generate a point every second following a normal distribution and update the plot with the last 10 points
def live_plot_distribution():
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)  
    ax.set_ylim(-3, 3)  
    ax.set_title('Updating Plot of Recent Points')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Value')
    lines, = ax.plot([], [], 'bo-') 
    
    recent_points = []
    
    """
    Generate a point every second following a normal distribution and update the plot with the last 10 points.

    Args:
        Generates a plot line with parameters
    Returns:
        graph
    """
    
    def init():
        """creates plot.
        Args:
            None
        Returns:
            lines: The initial empty line for the animation.
        """
        return lines,

    def update(frame):
        """Update the plot.
        Args:
            frame (int): The current frame number.
        Returns:
            lines (Line2D): The updated line for the animation.
        """
        
        new_point = np.random.normal(loc=0, scale=1)
        recent_points.append(new_point)
        if len(recent_points) > 10:
            recent_points.pop(0)

        
        lines.set_data(range(len(recent_points)), recent_points)
        return lines,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=1000)
    plt.show()


if __name__ == "__main__":
    plot_normal_distribution()  
    plot_line(y_intercept=0, slope=1, lower_x=-10, upper_x=10)  
    live_plot_distribution()  