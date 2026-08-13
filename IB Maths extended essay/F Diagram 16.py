import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import quad

# Parameters
L = 0.648  # Length of the string
N_terms = 100  # Number of Fourier coefficients
t_max = 2.0  # Maximum time in the physical system
x_points = 500  # Increased spatial resolution

# Calculate Fourier coefficients B_n and A_n more carefully
B_n = np.zeros(N_terms)
A_n = np.zeros(N_terms)

print("Calculating Fourier coefficients...")
for n in range(1, N_terms + 1):
    # Calculate the integral ∫sin(4.85nx)dx from 0 to L
    # Analytical solution: ∫sin(kx)dx = -cos(kx)/k
    k = 4.85 * n
    integral = (-np.cos(k * L) + np.cos(0)) / k
    # integral = (1 - np.cos(k * L)) / k
    
    B_n[n-1] = (2 / L) * integral
    A_n[n-1] = (-2.01e-3 / n) * integral
    
    # Print first few coefficients for debugging
    if n <= 5:
        print(f"n={n}: B_n = {B_n[n-1]:.6f}, A_n = {A_n[n-1]:.6f}")

# Check coefficient magnitudes
print(f"\nMax |B_n|: {np.max(np.abs(B_n)):.6f}")
print(f"Max |A_n|: {np.max(np.abs(A_n)):.6f}")

# Create spatial grid
x = np.linspace(0, L, x_points)

# Test the function at t=0 to see initial shape
def string_displacement(t):
    y = np.zeros_like(x)
    for n in range(1, N_terms + 1):
        term = (A_n[n-1] * np.sin(1530 * n * t) + 
                B_n[n-1] * np.cos(1530 * n * t)) * np.sin(4.85 * n * x)
        y += term
    return y

# Check initial displacement
y_initial = string_displacement(0)
print(f"\nInitial displacement range: [{np.min(y_initial):.6f}, {np.max(y_initial):.6f}]")

# Set up the figure and axis with appropriate limits
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Main animation plot
ax1.set_xlim(0, L)
# Auto-scale y-axis based on initial displacement
y_range = np.max(np.abs(y_initial)) * 1.5 if np.max(np.abs(y_initial)) > 0 else 0.01
ax1.set_ylim(-y_range, y_range)
ax1.set_xlabel('Position x (m)')
ax1.set_ylabel('Displacement y (m)')
ax1.set_title('linear wave with f(x)=1, g(x)=-1')
ax1.grid(True)

# Coefficient plot
n_values = np.arange(1, N_terms + 1)
ax2.semilogy(n_values, np.abs(B_n), 'ro-', markersize=2, label='|B_n|', alpha=0.7)
ax2.semilogy(n_values, np.abs(A_n), 'bo-', markersize=2, label='|A_n|', alpha=0.7)
ax2.set_xlabel('Fourier coefficient index n')
ax2.set_ylabel('Magnitude (log scale)')
ax2.set_title('Fourier Coefficient Magnitudes')
ax2.legend()
ax2.grid(True)

# Initialize the line
line, = ax1.plot([], [], 'b-', linewidth=2)

# Add time display
time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, fontsize=12,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

# Animation function
def animate(frame):
    # Convert frame to physical time (10x slower: 1s animation = 10s real)
    t_physical = frame * (t_max / 200)  # 200 frames total
    
    # Calculate string displacement
    y = string_displacement(t_physical)
    
    # Update the line
    line.set_data(x, y)
    
    # Update time display
    time_text.set_text(f'Time: {t_physical:.3f} ')
    
    return line, time_text

# Create animation
print("\nCreating animation...")
animation = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.tight_layout()
plt.show()

# Additional diagnostic plot
plt.figure(figsize=(10, 6))
for t in [0, 0.1, 0.2, 0.5]:
    y = string_displacement(t)
    plt.plot(x, y, label=f't = {t}s')
plt.xlabel('Position x (m)')
plt.ylabel('Displacement y (m)')
plt.title('linear wave with f(x)=1, g(x)=-1')
plt.legend()
plt.grid(True)
plt.show()