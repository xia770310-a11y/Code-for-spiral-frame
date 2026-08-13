import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipj
from scipy.special import ellipk

def cn(u, m):
    """Jacobi elliptic function cn(u, m)"""
    result = ellipj(u, m)
    return result[1]

# Parameters
m = 0.99  # parameter for cn function
K = ellipk(m)  # Complete elliptic integral of the first kind

# cn(2K·t, m) has period 1 (since cn(2K·(t+1), m) = cn(2K·t + 4K, m) = cn(2K·t, m))
# cos(πt) has period 2
# To compare them properly, let's plot over a range that shows their periods clearly

# Create time array (showing multiple periods)
t = np.linspace(0, 2, 2000)  # 4 units to show multiple periods

# Calculate functions
cos_pi_t = np.cos(np.pi * t)
cn_2K_t = cn(2 * K * t, m)

# Create the plot
plt.figure(figsize=(12, 6))

plt.plot(t, cos_pi_t, 'b-', linewidth=2, label='cos(3.14t) ')
plt.plot(t, cn_2K_t, 'r-', linewidth=2, label=f'cn(6.71·t, {m}) ')

plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.title('cos(3.14t) and cn(6.71·t, 0.99)')
plt.legend(loc='lower left')
plt.grid(True, alpha=0.3)
plt.ylim(-1.5, 1.5)




plt.tight_layout()
plt.show()

print(f"Complete elliptic integral K(0.99) = {K:.6f}")
print(f"cn(2K·t, 0.99) ")
print(f"cos(πt) ")
print(f"Ratio of periods: cos(πt) period / cn(2K·t) period = 2")