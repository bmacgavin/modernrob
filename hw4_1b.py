# Imports
import numpy as np

# Simplify the print outputs
np.set_printoptions(suppress=True)

# Define the angles in degrees and convert them to radians
theta = np.sqrt(5)

# Obtain the skew-symmetric matrices for each of the axes around which rotations happen
w_hat_bracket = np.array([[0, 0, 2*np.sqrt(5)/5], 
                          [0, 0, -np.sqrt(5)/5], 
                          [-2*np.sqrt(5)/5, np.sqrt(5)/5, 0]])


# Calculate the rotation matrices using Rodrigue's formula
w_hat_bracket_theta = np.identity(3) + np.sin(theta)*w_hat_bracket + (1-np.cos(theta))*np.matmul(w_hat_bracket,w_hat_bracket)

# Print the final rotation matrix
print(w_hat_bracket_theta)
