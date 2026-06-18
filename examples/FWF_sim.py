# -*- coding: utf-8 -*-


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add MinGW DLL path (if required for EWF_pybind)
os.add_dll_directory("C:\\mingw64\\bin")

import EWF_pybind as EWF  # make sure EWF_pybind is installed and built properly

# ---------------------------------------------------------------------
# 1. Load CSV data (1000x4 matrix)
# ---------------------------------------------------------------------
csv_path = "C:\\Users\\User\\Documents\\FWF\\subordinator_simulations.csv"
data = pd.read_csv(csv_path)  # assume no header row
n_rows, n_cols = data.shape
print(f"Loaded data with shape: {data.shape}")

# ---------------------------------------------------------------------
# 2. Define Wright–Fisher parameters
# ---------------------------------------------------------------------
m1, m2 = 1, 1
mutation_vector = np.array([m1, m2])
non_neutral = False
sigma = 0
selectionSetup = 0
dominance_parameter = 0.0
selectionPolynomialDegree = 1
selectionCoefficients = np.array([])

WF = EWF.WrightFisher(
    mutation_vector,
    non_neutral,
    sigma,
    selectionSetup,
    dominance_parameter,
    selectionPolynomialDegree,
    selectionCoefficients
)

# ---------------------------------------------------------------------
# 3. Simulation parameters
# ---------------------------------------------------------------------
nSim = 10
x = 0.5
startT = 0.0
Absorption = False
par1 = 1
subName = "N"  # 'N' (none), 'A' (alpha-stable), 'P' (Poisson), etc.

# ---------------------------------------------------------------------
# 4. Run simulations for each column
# ---------------------------------------------------------------------
simulation_results = []  # to store simulation outputs per column

for col_idx in range(n_cols):
    times = data.iloc[:, col_idx].dropna().values  # ensure numeric & drop any NaNs
    col_results = []
    
    for t in times:
        # Run diffusion simulation for each time
        tempOut = WF.DiffusionRunner(
            nSim, x, startT, float(t), par1, subName, Absorption,
            f"EFWF_diffusion_col{col_idx}_t{t:.3f}_sim.txt"
        )
        col_results.append(tempOut)
    
    simulation_results.append(col_results)
    print(f"Finished column {col_idx + 1}/{n_cols}")


