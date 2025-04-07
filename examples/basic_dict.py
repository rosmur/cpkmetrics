from src.cpkmetrics.process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 10
stddev = 1
USL = 14
LSL = 6

# Create an instance of the ProcessCapability class with the provided parameters. Instantiation also automatically prints results to the terminal
pc = ProcessCapability(mean, stddev, USL, LSL, print_results=False)

# The calculated metrics are available to access as a dictionary through the metrics method:
print(
    f"All computed items are available as a {type(pc.metrics)} through the metrics method. \n \n"
)

# You can access specific metrics by key:
cpk = pc.metrics["Process Capability Index"]
print(f"The Cpk is {round(cpk, 2)} \n \n")

# Or you can iterate through the metrics dictionary:
for key, value in pc.metrics.items():
    print(f"{key}: {value}")
