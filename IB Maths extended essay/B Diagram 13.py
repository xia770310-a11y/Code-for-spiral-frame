import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipj

# Parameters
eccentricity = 0.701
frequency = 62200
t_end = 1.2e-4

# Create time array
t = np.linspace(0, t_end, 1000)

# Calculate the arguments for the elliptic functions
u = frequency * t
m = eccentricity**2  # scipy uses parameter m = k^2

# Calculate sn and cn values
sn_values, cn_values, dn_values, ph = ellipj(u, m)


plt.figure(figsize=(10, 6))
plt.plot(t, sn_values, 'b-', linewidth=2, label=f'sn(62200t, {eccentricity})')
plt.plot(t, cn_values, 'r-', linewidth=2, label=f'cn(62200t, {eccentricity})')
plt.xlabel('Time (s)')
plt.ylabel('Function Value')
plt.title(f'cn(62200t, 0.701) and sn(62200t, 0.701)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Print some properties
print(f"Eccentricity k = {eccentricity}")
print(f"Parameter m = k² = {m:.6f}")
print(f"Time range: 0 to {t_end} s")
print(f"Frequency: {frequency} Hz")
print(f"Number of periods in range: approximately {frequency * t_end:.2f}")