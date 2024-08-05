from process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 9
stddev = 0.2
USL = 12.0
LSL = 8.0

# Create an instance of the ProcessCapability class with the provided parameters. Instantiation also automatically prints results to the terminal
pc = ProcessCapability(mean, stddev, USL, LSL)

# The calculated metrics are available (as a dictionary):
print(pc.metrics)
