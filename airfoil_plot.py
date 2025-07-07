import numpy as np
import matplotlib.pyplot as plt

# Settings
fs = 12
lw = 2

# Load data
profile1 = np.loadtxt('./Profiles/PolarsFFA-W3-241.txt')
profile2 = np.loadtxt('./Profiles/PolarsFFA-W3-480.txt')

xP1, yP1 = profile1[:, 0], profile1[:, 1]
xP2, yP2 = profile2[:, 0], profile2[:, 1]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(xP1, yP1, label='FFA-W3-241', linewidth=lw)
plt.plot(xP2, yP2, label='FFA-W3-480', linewidth=lw)

plt.xlabel('x [-]', fontsize=fs)
plt.ylabel('y [-]', fontsize=fs)
plt.legend(fontsize=fs)
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.show()