from process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 9
stddev = 0.2
USL = 12.0
LSL = 8.0

# Create an instance of the ProcessCapability class with the provided parameters
pc = ProcessCapability(mean, stddev, USL, LSL, print_results=False)

cpk = pc.Cpk()

print(cpk)