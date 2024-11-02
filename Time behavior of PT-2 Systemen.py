# -*- coding: utf-8 -*-
"""
Created on Sat Nov 2  2021

@author: theha
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate damping ratio using two consecutive overshoots (Method a)
def damping_from_overshoots(y1, y2):
    return 1 / np.sqrt(1 + (2 * np.pi / np.log(y1 / y2))**2)

# Function to calculate damping ratio using the first overshoot and steady-state value (Method b)
def damping_from_first_overshoot(y1, y_inf):
    return np.sqrt(np.log(y1 / y_inf)**2 / (np.pi**2 + np.log(y1 / y_inf)**2))

# Function to calculate characteristic angular frequency ω0
def characteristic_angular_frequency(T_d, D):
    omega_d = 2 * np.pi / T_d  # Damped natural frequency
    return omega_d / np.sqrt(1 - D**2)

# Function to simulate the damped oscillation response
def simulate_response(K, omega_0, D, time_span, time_step=0.01):
    t = np.arange(0, time_span, time_step)
    omega_d = omega_0 * np.sqrt(1 - D**2)
    response = K * (1 - np.exp(-D * omega_0 * t) * (np.cos(omega_d * t) + (D / np.sqrt(1 - D**2)) * np.sin(omega_d * t)))
    return t, response

# Inputs
y1 = float(input("Enter the first overshoot value: "))
y2 = float(input("Enter the second overshoot value: "))
y_inf = float(input("Enter the steady-state value: "))
T_d = float(input("Enter the time between overshoots: "))

# Calculate parameters
K = y_inf  # Assuming unit step input
D_a = damping_from_overshoots(y1, y2)
D_b = damping_from_first_overshoot(y1, y_inf)
omega_0_a = characteristic_angular_frequency(T_d, D_a)
omega_0_b = characteristic_angular_frequency(T_d, D_b)

# Simulate response for both damping ratios
time_span = 10  # Total time for simulation
t_a, response_a = simulate_response(K, omega_0_a, D_a, time_span)
t_b, response_b = simulate_response(K, omega_0_b, D_b, time_span)

# Plotting the responses
plt.figure(figsize=(12, 6))

# Method a plot
plt.subplot(1, 2, 1)
plt.plot(t_a, response_a, label="Response (Method a)", color='b')
plt.axhline(y=K, color='gray', linestyle='--', label="Steady-State Value")
plt.scatter([0, T_d], [y1, y2], color='red', label="Overshoots")
plt.title(f"Method a: D = {D_a:.3f}, ω₀ = {omega_0_a:.3f}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Method b plot
plt.subplot(1, 2, 2)
plt.plot(t_b, response_b, label="Response (Method b)", color='g')
plt.axhline(y=K, color='gray', linestyle='--', label="Steady-State Value")
plt.scatter([0, T_d], [y1, y2], color='red', label="Overshoots")
plt.title(f"Method b: D = {D_b:.3f}, ω₀ = {omega_0_b:.3f}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.suptitle("System Response with Different Damping Ratios")
plt.tight_layout()
plt.show()

# Output results
print(f"Gain K = {K}")
print(f"Damping ratio (Method a) D = {D_a}")
print(f"Characteristic angular frequency (Method a) ω0 = {omega_0_a}")
print(f"Damping ratio (Method b) D = {D_b}")
print(f"Characteristic angular frequency (Method b) ω0 = {omega_0_b}")
