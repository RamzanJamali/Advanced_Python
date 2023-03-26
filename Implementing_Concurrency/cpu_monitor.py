# This code is monitoring CPU usage and displaying it on a graph in real-time using the RxPy library.

from rx import interval
from rx.operators import map, publish, buffer_with_count
# First, it imports necessary libraries including "interval" which creates an observable that emits sequential 
# numbers at a specified interval, "map" which applies a function to each emitted value, "publish" which 
# multicasts a single source observable sequence to multiple observers, and "buffer_with_count" which buffers 
# the specified number of items emitted by an observable sequence.
import psutil
import numpy as np
# It also imports "psutil" which is a Python library for retrieving information on running processes and 
# system utilization (including CPU usage). It also imports "numpy" for numerical computations and "pylab" 
# which provides a MATLAB-like plotting framework.
import pylab as plt


# Next, it defines an observable sequence "cpu_data" that publishes CPU usage percentage at a 0.1-second interval.
cpu_data = publish()(map(lambda x: psutil.cpu_percent())(interval(0.1)))
cpu_data.connect()

# Then, it defines the function "monitor_cpu" which takes a parameter npoints, which specifies the number of 
# data points to display on the graph.
def monitor_cpu(npoints):
    (lines, ) = plt.plot([], [])
    plt.xlim(0, npoints)
    plt.ylim(0, 100)

    # Inside "monitor_cpu", it sets up the graph using "pylab" and initializes the CPU data window 
    # using the "buffer_with_count" operator.
    cpu_data_window = buffer_with_count(npoints, 1)(cpu_data)

    # It defines a function "update_plot" which updates the plot with the latest CPU usage data. It also 
    # defines a function "update_warning" which updates a text label indicating whether the CPU usage is normal or high.
    def update_plot(cpu_readings):
        lines.set_xdata(np.arange(len(cpu_readings)))
        lines.set_ydata(np.array(cpu_readings))
        plt.draw()

    alterpoints = 4
    
    # It sets up an observable "high_cpu" that emits "True" when the CPU usage is consistently high 
    # (i.e., all readings in the buffer are greater than 20%).
    high_cpu = map(lambda readings: all(r > 20 for r in readings))(buffer_with_count(alterpoints, 1)(cpu_data))

    label = plt.text(1, 1, "Normal")

    def update_warning(is_high):
        if is_high:
            label.set_text("High")
        else:
            label.set_text("Normal")

    # Finally, it subscribes to "high_cpu" and "cpu_data_window" observables and updates the plot and warning label 
    # accordingly. It then shows the plot using "plt.show()".
    high_cpu.subscribe(update_warning)
    cpu_data_window.subscribe(update_plot)

    plt.show()


# It calls "monitor_cpu" with an argument of 100, which specifies the number of data points to display on the graph.
if __name__ == "__main__":
    monitor_cpu(100)
