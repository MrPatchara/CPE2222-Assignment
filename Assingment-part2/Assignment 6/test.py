import pandas as pd
import numpy as np

# Assuming 'df' is your DataFrame and you have a specific index i for each operation.
# Initialize your list D to store the data
D = []

# Sample DataFrame for illustration purposes
data = {
    'column1': ['7.518413695614470926e-01', '6.205482694093682472e-01', '3.024628286619701623e-02'],
    'column2': ['4.697197519452689374e-02', '7.357883146647291595e-01', '8.958430645037536166e-01']
}

df = pd.DataFrame(data)

# Convert all values in the DataFrame to float (handle potential non-numeric values)
df = df.apply(pd.to_numeric, errors='coerce')

# If you're trying to store the values from each row into D[i]
for i in range(len(df)):  # Loop over rows
    # Convert the row values to a numpy array of floats and store it in D[i]
    D.append(df.iloc[i].values.astype(float))  # Store each row as a list of floats

# Alternatively, if you need to access and process each row individually
for i in range(len(df)):
    D[i] = df.iloc[i].values.astype(float)  # Store the values of each row as a float array

# Print the result to verify
print(D)
