"""
The ProcessCapability package can be used with DataFrames containing statistics and spec limits easily. Here we show how to do this with sample data, here loaded from a CSV where process capability metrics are calculated and added to the original dataframe as new columns.
"""

import pandas as pd
from src.cpkmetrics.process_capability import ProcessCapability

df = pd.read_csv("examples/sample_input.csv")


def calculate_metrics(row):
    pc = ProcessCapability(
        row["mean"], row["stddev"], row["USL"], row["LSL"], print_results=False
    )
    return pd.Series(pc.metrics)


# Apply the function to each row and create new columns
new_columns = df.apply(calculate_metrics, axis=1)

# Concatenate the new columns with the original DataFrame
result_df = pd.concat([df, new_columns], axis=1)

# Now result_df contains all the original columns plus the new metric columns
print(result_df)

# Save to CSV for easy visibility of results in this example
result_df.to_csv("examples/sample_output.csv", index=False)
