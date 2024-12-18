import unittest
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

class TestFunctions(unittest.TestCase):

    def test_plot_normal_distribution(self):
        """Test that 200 points are generated from a normal distribution."""
        data = plot_normal_distribution()
        self.assertEqual(len(data), 200)  # Check if 200 points are generated
        self.assertAlmostEqual(np.mean(data), 0, delta=0.5)  # Mean should be close to 0
        self.assertAlmostEqual(np.std(data), 1, delta=0.5)  # Std deviation should be close to 1

    def test_plot_line(self):
        """Test that the line function generates correct x and y values."""
        y_intercept = 2
        slope = 3
        lower_x = -5
        upper_x = 5

        x_values, y_values = plot_line(y_intercept, slope, lower_x, upper_x)
        self.assertEqual(len(x_values), 100)  # Ensure 100 points are generated
        self.assertEqual(len(y_values), 100)  # Ensure y matches x in length
        self.assertAlmostEqual(y_values[0], slope * x_values[0] + y_intercept)  # Test the first point
        self.assertAlmostEqual(y_values[-1], slope * x_values[-1] + y_intercept)  # Test the last point

    def test_live_plot_distribution(self):
        """Test the live plot for correct initialization."""
        # This function can't be fully tested for visuals, but we can test the logic.
        # For example, we can simulate the `recent_points` list.
        recent_points = []
        for _ in range(15):
            new_point = np.random.normal(loc=0, scale=1)
            recent_points.append(new_point)
            if len(recent_points) > 10:
                recent_points.pop(0)
        self.assertEqual(len(recent_points), 10)  # Ensure only the last 10 points are retained

if __name__ == "__main__":
    unittest.main(exit=False)  # Run the tests and keep the script running

    # Run the functions for demonstration
    plot_normal_distribution()
    plot_line(y_intercept=0, slope=1, lower_x=-10, upper_x=10)
    live_plot_distribution()