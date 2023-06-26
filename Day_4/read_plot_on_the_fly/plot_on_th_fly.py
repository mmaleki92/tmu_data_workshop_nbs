import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np

app = pg.mkQApp("Plotting Example")

# Create a plot window
win = pg.GraphicsLayoutWidget(title="Animation Example")
plot = win.addPlot()

# Initialize the data
data = []

# Create a plot curve
curve = plot.plot(data, pen='b')

# Open the file for reading
file_path = "data.txt"
file = open(file_path, 'r')

# Define the update function
def update():
    # Read values from the file
    lines = file.readlines()
    new_data = [float(line.strip()) for line in lines]

    # Append new data to the data array
    data.extend(new_data)

    # Update the plot curve with the new data
    curve.setData(data[-100:])

# Create a timer
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)  # Update every 100 milliseconds (10 times per second)
win.show()

# Start the Qt event loop
app.exec()

# Clean up
file.close()
