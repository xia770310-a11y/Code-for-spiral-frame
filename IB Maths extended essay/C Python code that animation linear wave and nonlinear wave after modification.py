import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk, ellipj

# Parameters
m = 0.491
A = 9900
f = 62200
horizontal_value = 244

# Calculate period of dn function
K = ellipk(m)  # Complete elliptic integral of the first kind
period_u = 2 * K  # Period in the u domain
period_t = period_u / f  # Period in the t domain

# Create time array for two periods
t_two_periods = np.linspace(0, 2 * period_t, 1000)

# Compute dn function
u_vals = f * t_two_periods
# ellipj(u, m) returns (sn, cn, dn, ph)
_, _, dn_vals, _ = ellipj(u_vals, m)
f_dn_vals = A * dn_vals

# Create the horizontal line array
f_horizontal = np.full_like(t_two_periods, horizontal_value)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(t_two_periods, f_dn_vals, 'b-', label=r'$f_{\mathrm{inst}}(t) $=9900dn(62200t, 0.701) ', linewidth=2)
plt.plot(t_two_periods, f_horizontal, 'r--', label=r'$f_{\mathrm{inst}}(t) $=244' , linewidth=2)

plt.xlabel('Time $t$ (s)')
plt.ylabel('$f_{\mathrm{inst}}(t)$')
plt.title('9900dn(62200t, 0.701) and 244')
plt.grid(True, alpha=0.3)

# Move legend outside the graphing area
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')



plt.tight_layout()
plt.show()
