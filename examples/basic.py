"""
A "Hello World" example of using the cpkmetrics package.

This example shows calculation of Cpk for a given input of mean, standard deviation and spec limits.

----
NOTES:
    - cpkmetrics package should be installed prior to use
"""

from cpkmetrics.process_capability import ProcessCapability

# Example values for mean, stddev, USL, and LSL
mean = 10  # Average
stddev = 1  # Standard Deviation
USL = 14  # Upper Spec Limit
LSL = 6  # Lower Spec Limit

# Create an instance of the ProcessCapability class with the provided parameters.
# Instantiation also automatically prints results to the terminal (the print_results arg defaults to True)
pc = ProcessCapability(mean, stddev, USL, LSL)

# You can also access individual items directly through the corrresponding property
cpk = pc.process_capability_index

print(f"The Cpk is {round(cpk, 2)}")
