import numpy as np

# Load data from files and create variable D
file_names = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv"]
D = []

# Load data from each file
for file in file_names:
    data = np.loadtxt(file, delimiter=" ")
    D.append(data)

D = np.array(D)  # D should have shape (5, 100, 100)
print("Shape of D:", D.shape)  # Confirm shape

# Calculate X as the mean of D along axis 1
X = D.mean(axis=1)  # X will have shape (5, 100)
X = X.T  # Transpose to shape (100, 5)
print("X[0,:] =", X[0])  # Check first row of X
print("X[-1,:] =", X[-1])  # Check last row of X

# Calculate Y as the standard deviation of D along axis 1, then reshape it to (100, 1)
Y = D.std(axis=1)  # Standard deviation along axis 1
Y = Y.reshape(100, 5)  # Reshape to (100, 5)
print("Y[0,0] =", Y[0, 0])  # Check first element of Y
print("Y[-1,0] =", Y[-1, 0])  # Check last element of Y

# Calculate A as the sum of D along axes 1 and 2
A = D.sum(axis=(1, 2)).reshape(1, 5)  # A will have shape (1, 5)
print("A =", A)  # Check A

# Compute J
J = np.sum((X - np.mean(X, axis=0)) ** 2)

# Compute K
K = np.mean(X, axis=0).reshape(1, -1) * 10000

# Print the results
print(f"X[0,:] = {X[0, :5]}")
print(f"X[-1,:] = {X[-1, :5]}")
print(f"Y[0,0] = {Y[0, 0]}")
print(f"Y[-1,0] = {Y[-1, 0]}")
print(f"A = {A}")
print(f"J = {J}")
print(f"K = {K[:, :5]}")