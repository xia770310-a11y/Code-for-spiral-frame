import numpy as np
 import matplotlib.pyplot as plt
 from matplotlib.animation import FuncAnimation from scipy.special import ellipj
 import warnings warnings.filterwarnings('ignore')
					
# Set up the figure and axes
 fig, ax = plt.subplots(figsize=(12, 6))
					
# Define the x domain
 x = np.linspace(0, 0.648, 500)
					
# Define the time range and create time array t_start, t_end = 0, 0.005
 t_values = np.linspace(t_start, t_end, 200)
					
# Initialize the plots
 line1, = ax.plot(x, np.zeros_like(x), 'b-', linewidth=2, label='cn(62200t, 0.701)sin(4.85x)')
 line2, = ax.plot(x, np.zeros_like(x), 'r-', linewidth=2, label='cos(1530t)sin(4.85x)')
					
# Set up the axes
ax.set_xlim(0, 0.648)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('x')
ax.set_ylabel('y(x,t)')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')

# Create a timer box in the top-left corner
timer_box = ax.text(0.02, 0.98, 'Time: 0.00000 s', transform=ax.transAxes,
fontsize=12, verticalalignment='top',
bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='black'))
# Function 1: Using Jacobi elliptic cosine (cn) def function1(x, t):
# For scipy, ellipj(u, m) where m = k^2 # Here k = 0.701, so m = 0.701^2
m = 0.701**2
u = 62200 * t
# ellipj returns (sn, cn, dn, ph) cn_val = ellipj(u, m)[1]
return cn_val * np.sin(4.85 * x)
# Function 2: Absolute value of cosine times sine def function2(x, t):
return np.cos(1530 * t) * np.sin(4.85 * x)
# Animation update function def update(frame):
t = t_values[frame]
# Update both functions y1 = function1(x, t)
y2 = function2(x, t)
line1.set_ydata(y1) line2.set_ydata(y2)
# Update timer box with current time timer_box.set_text(f'Time: {t:.5f} s')
return line1, line2, timer_box
animation = FuncAnimation(fig, update, frames=len(t_values), interval=50, blit=False, repeat=True)
ax.set_title(f'cos(1530t)sin(4.85x) and cn(62200t, 0.701)sin(4.85x)')
plt.tight_layout() plt.show()
