import matplotlib.pyplot as plt
import numpy as np

Ts = 30   # signal interval
end = 150  # signal end point
n = int(end/Ts)+1

x = np.linspace(0, end, num=n)  # signal vector

#TODO: revise this array to your results
y = np.array([0.000, 6.619, 10.766, 11.723, 11.005, 11.5649])  # speed vector (ccw)
#y = np.array([0.000, 5.263, 10.447, 11.643, 11.962, 11.883])  # speed vector (cw)

# Least squares polynomial fit, and return the coefficients.
z = np.polyfit(x, y, 2)

goal = 8             # if we want to let the servo run at 7 cm/sec
# equation : z[0]*x^2 + z[1]*x + z[2] = goal
z[2] -= goal         # z[0]*x^2 + z[1]*x + z[2] - goal = 0

# Return the roots of a polynomial with coefficients given
result = np.roots(z)

# output the correct one
if (0 <= result[0]) and (result[0] <= end):
    print(result[0])
else:
    print(result[1])
