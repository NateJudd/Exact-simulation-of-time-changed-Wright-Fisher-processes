import os
os.add_dll_directory("C:\\mingw64\\bin")

import EWF_pybind as EWF
import numpy as np
import matplotlib.pyplot as plt 

new_directory_path = "C:\\Users\\User\\EWF-main\\paper\\Oct25"
os.chdir(new_directory_path)
# Simple python script to construct Wright--Fisher class and run diffusion simulator

# Define Wright--Fisher diffusion class parameters
m1 = 3
m2 = 8
mutation_vector = np.array([m1, m2])
non_neutral = False
sigma = 0
selectionSetup = 0
dominance_parameter = 0.0
selectionPolynomialDegree = 1
selectionCoefficients = np.array([])

# Create and initialise WrightFisher class
WF = EWF.WrightFisher(mutation_vector, non_neutral, sigma, selectionSetup, dominance_parameter, selectionPolynomialDegree, selectionCoefficients)

# Define simulation parameters
nSim = 100000
x = 0.5
startT = 0.0
endT = 0.25# 0.1,0.5,1,2 (not 5)
Absorption = False


par1 = 1# 0.5,100, 0;5
subName = 'T' #N (none),A (alpha-stable),P (poisson process), T (inverse-gaussian / tilted positive 1/2-stable), G (gamma process)

#fix theta case

# create data output filename
Filename_sim = "EWF_diffusion_" + str(m1)+","+str(m2)+","+subName+str(par1)+",t"+str(endT)+ "_sim.txt"


# Run simulator
WF.DiffusionRunner(nSim, x, startT, endT, par1, subName, Absorption, Filename_sim)

# Define parameters for pointwise transition density evaluation
meshSize = 100
Filename_eva = "EWF_diffusion_" + str(m1)+","+str(m2) + "_eva.txt"


# Run transition density evaluator
#WF.DiffusionDensityCalculator(meshSize, x, startT, endT, par1, subName, Absorption, Filename_eva)

# Load in data, create histogram and generate plot
data = np.loadtxt(Filename_sim)
#density = np.loadtxt(Filename_eva)
Filename_png = "EWF_diffusion_" + str(m1)+","+str(m2)+","+subName+str(par1)+",t"+str(endT)+ ".png"

# WANT: DENSITY ONLY

fig, ax = plt.subplots(1,1)
counts = plt.hist(data, bins=50, density=True)
#ax.plot(density[density[:, 1] <= max(counts[0]), 0], density[density[:, 1] <= max(counts[0]), 1], linewidth = 2)
#ax.set_xlabel("Sample draws")
ax.set_ylabel("Density")
#ax.set_title("Histogram of sample draws (blue)")
plt.savefig(Filename_png)
plt.close()