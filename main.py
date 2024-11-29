import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function to plot 200 points sampled from a standard normal distribution
def plot_normal_distribution():
    """Plot 200 points sampled from a standard normal distribution."""
    # Sample 200 points from standard normal distribution
    data = np.random.randn(200)

    # Create a histogram of the data
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, alpha=0.7, color='blue')
    plt.title('Histogram of 200 Points from Standard Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

# Define the function to plot a line given y-intercept, slope, and x boundaries
def plot_line(y_intercept, slope, lower_x, upper_x):
    """Plot a line defined by y_intercept and slope within specified x boundaries."""
    # Generate x values
    x_values = np.linspace(lower_x, upper_x, 100)
    # Calculate y values based on the line equation y = mx + b
    y_values = slope * x_values + y_intercept

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, color='red', label=f"y = {slope}x + {y_intercept}")
    plt.title('Line Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(lower_x * slope + y_intercept - 10, upper_x * slope + y_intercept + 10) # Adjust y limits
    plt.xlim(lower_x, upper_x)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid()
    plt.legend()
    plt.show()

# Define the function to generate points every second, updating a graph live
def live_plot_distribution():
    """Generate a point every second following a normal distribution and update the plot with the last 10 points."""
    plt.style.use('fivethirtyeight')

    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)   # Set x-axis limits
    ax.set_ylim(-3, 3)   # Set y-axis limits
    ax.set_title('Live Updating Plot of Recent Points')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Value')
    lines, = ax.plot([], [], 'bo-')  # line initialized

    # Prepare to store recent points
    recent_points = []

    def init():
        """Initialize empty plot."""
        return lines,

    def update(frame):
        """Update the plot with new random point."""
        # Generate a new point from standard normal distribution
        new_point = np.random.normal(loc=0, scale=1)
        recent_points.append(new_point)

        # Keep only the last 10 points
        if len(recent_points) > 10:
            recent_points.pop(0)

        # Update the line plot
        lines.set_data(range(len(recent_points)), recent_points)
        return lines,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=1000)
    plt.show()

# Test the functions
if __name__ == "__main__":
    plot_normal_distribution()   # Test 1: Plot standard normal distribution
    plot_line(y_intercept=0, slope=1, lower_x=-10, upper_x=10)  # Test 2: Plot line
    live_plot_distribution()  # Test 3: Live-updating plot of distribution