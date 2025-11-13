import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import matplotlib.cm as cm

# Define all groups in one place
groups = {
    "N1": {"m1": 0.5, "m2": 0.5, "param": "N1"},
    "N2": {"m1": 1, "m2": 1, "param": "N1"},
    "N3": {"m1": 2, "m2": 2, "param": "N1"},
    "N4": {"m1": 0.3, "m2": 0.7, "param": "N1"},
    "N4": {"m1": 0.4, "m2": 0.6, "param": "N1"},
    "N4": {"m1": 0.45, "m2": 0.55, "param": "N1"},
    "N4": {"m1": 3, "m2": 8, "param": "N1"},
    "A1": {"m1": 0.5, "m2": 0.5, "param": "A0.5"},
    "A2": {"m1": 1, "m2": 1, "param": "A0.5"},
    "A3": {"m1": 2, "m2": 2, "param": "A0.5"},
    "A4": {"m1": 0.45, "m2": 0.55, "param": "A0.5"},
    "A4": {"m1": 3, "m2": 8, "param": "A0.5"},
    "P2": {"m1": 1, "m2": 1, "param": "P100"},
    "G1": {"m1": 0.5, "m2": 0.5, "param": "G2"},
    "G2": {"m1": 1, "m2": 1, "param": "G2"},
    "G3": {"m1": 2, "m2": 2, "param": "G2"},
    "G4": {"m1": 0.3, "m2": 0.7, "param": "G2"},
    "G4": {"m1": 3, "m2": 8, "param": "G2"},
    "T1": {"m1": 0.5, "m2": 0.5, "param": "T1"},
    "T2": {"m1": 1, "m2": 1, "param": "T1"},
    "T3": {"m1": 2, "m2": 2, "param": "T1"},
    "T4": {"m1": 3, "m2": 8, "param": "T1"}
}

# Select which version to plot
ver = "G3"  # change to "N", "A", "P", or "G"

# Extract parameter info for that version
m1 = groups[ver]["m1"]
m2 = groups[ver]["m2"]
param = groups[ver]["param"]

# Simulation times
times = [0.25, 0.5, 1, 2]
labels = [f"t={t}" for t in times]
colors = (cm.inferno(np.linspace(0.9,0.2,len(times)))) #["blue", "orange", "green", "red"]

# Build the filenames dynamically
filenames = [f"EWF_diffusion_{m1},{m2},{param},t{t}_sim.txt" for t in times]

plt.figure(figsize=(8, 6))

for file, label, color in zip(filenames, labels, colors):
    # Load data
    data = np.loadtxt(file)
    
    # Plot histogram (semi-transparent)
    #plt.hist(data, bins=50, density=True, alpha=0.3, color=color, label=f"{label} (hist)")
    
    # Add a smooth density estimate
    kde = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 500)
    plt.plot(x_vals, kde(x_vals), color=color, linewidth=2, label=f"{label}")

# Axis labels and title
plt.xlabel("Sample draws")
plt.ylabel("Density")
plt.title("Density Estimates of draws from t-WF transition functions")

# Legend
plt.legend()

# Save figure
figname = "EWF_diffusion_all_times_"+str(m1)+","+str(m2)+","+str(ver)+".png"
plt.savefig(figname, dpi=300)
plt.show()

