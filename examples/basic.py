from src.cpkmetrics.process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 10
stddev = 1
USL = 14
LSL = 6

# Create an instance of the ProcessCapability class with the provided parameters. Instantiation also automatically prints results to the terminal (unless you pass print_results=False arg)
pc = ProcessCapability(mean, stddev, USL, LSL)

# You can also access individual items directly through the corrresponding property
cpk = pc.process_capability_index

print(f"The Cpk is {round(cpk, 2)}")
