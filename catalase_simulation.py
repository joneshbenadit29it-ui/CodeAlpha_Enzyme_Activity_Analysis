import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# SETUP SIMULATION PARAMETERS (Michaelis-Menten Kinetics)
# ---------------------------------------------------------
# Vmax: Maximum velocity of the reaction (mmol/L/min)
# Km: Michaelis constant (mmol/L) - substrate conc. at 1/2 Vmax
Vmax = 150.0  
Km = 25.0     

# Generate simulated substrate concentrations [S] from 0 to 200 mmol/L
substrate_concentration = np.linspace(0, 200, 100)

# Calculate Reaction Velocity (V) using the Michaelis-Menten equation:
# V = (Vmax * [S]) / (Km + [S])
reaction_velocity = (Vmax * substrate_concentration) / (Km + substrate_concentration)

# Introduce minor random experimental noise to simulate realistic lab conditions
np.random.seed(42)  # For reproducible "experimental" variation
noise = np.random.normal(0, 2.5, size=substrate_concentration.shape)
simulated_velocity = np.clip(reaction_velocity + noise, 0, None)

# ---------------------------------------------------------
# GENERATE REPORT PLOT
# ---------------------------------------------------------
plt.figure(figsize=(9, 5.5))
plt.plot(substrate_concentration, reaction_velocity, 'r--', label='Theoretical Ideal Model', linewidth=2)
plt.scatter(substrate_concentration[::4], simulated_velocity[::4], color='blue', alpha=0.7, label='Simulated Data Points (Lab Trials)')

# Annotating key kinetic points
plt.axhline(y=Vmax, color='gray', linestyle=':', label=f'Vmax ({Vmax} mmol/L/min)')
plt.axhline(y=Vmax/2, color='green', linestyle=':', label=f'1/2 Vmax ({Vmax/2} mmol/L/min)')
plt.axvline(x=Km, color='purple', linestyle=':', label=f'Km ({Km} mmol/L)')

# Labels and Styling
plt.title("Virtual Lab: Effect of Substrate Concentration on Catalase Activity", fontsize=12, fontweight='bold')
plt.xlabel("Substrate Concentration [H₂O₂] (mmol/L)", fontsize=10)
plt.ylabel("Reaction Velocity (mmol/L/min)", fontsize=10)
plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.5)

# Save the plot automatically as a screenshot/image for documentation
plt.savefig('catalase_activity_curve.png', dpi=300)
print("Simulation complete! Graph saved as 'catalase_activity_curve.png'.")
plt.show()