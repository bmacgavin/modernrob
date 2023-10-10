import matplotlib.pyplot as plt
import numpy as np

# Given rotation matrix
Rsa = [[0, -1, 0],[0, 0, -1],[1,0,0]]
identity = np.identity(3)

# Find theta
theta = np.arccos((Rsa[0][0]+Rsa[1][1]+Rsa[2][2] - 1) / 2)
if np.sin(theta) != 0:
    theta_neg = 0 - theta
    w_hat_skew = (1/(2*np.sin(theta)))*(Rsa-np.transpose(Rsa))
    w_hat_skew_neg = (1/(2*np.sin(theta_neg)))*(Rsa-np.transpose(Rsa))
    w_hat_skew_neg = np.transpose(w_hat_skew_neg)

    # Create vectors for the coordinate frame
    origin = np.zeros(3)
    x_axis = w_hat_skew[0]
    x_axis_neg = w_hat_skew_neg[0]
    y_axis = w_hat_skew[1]
    y_axis_neg = w_hat_skew_neg[1]
    z_axis = w_hat_skew[2]
    z_axis_neg = w_hat_skew_neg[2]

    # Visualize the coordinate frame
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(*origin, *x_axis, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()

    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')
    ax.quiver(*origin, *x_axis_neg, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis_neg, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis_neg, color='b', label='Z-axis')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()

# elif np.sin(theta) == 0 and (theta/np.pi)%2 != 0:
#     w_hat_skew = np.sqrt((Rsa - identity) / 2)
#     print(theta)
#     print(w_hat_skew)
