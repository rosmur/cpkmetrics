from process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 10
stddev = 1
USL = 14
LSL = 6

# Create an instance of the ProcessCapability class with the provided parameters. Instantiation also automatically prints results to the terminal
pc = ProcessCapability(mean, stddev, USL, LSL)

# The calculated metrics are available (as a dictionary):
print(pc.metrics)
