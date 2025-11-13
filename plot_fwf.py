import os
os.add_dll_directory("C:\\mingw64\\bin")

import numpy as np
import matplotlib.pyplot as plt 

vector = []
with open('C:\\Users\\User\\Documents\\FWF\\merged_output.txt', 'r') as file:
    for line in file:
        # Strip leading/trailing whitespaces and split by spaces
        numbers = line.strip().split()
        
        # Convert each number to a float and append to the vector
        vector.extend([float(num) for num in numbers])

# Print the vector
print(vector)
Filename_png = "C:\\Users\\User\\Documents\\FWF\\EFWF_diffusion.png"


counts = plt.hist(vector, bins=50, density=True)
plt.xlabel('Sample draws')
plt.ylabel('Count')
plt.title("Histogram of draws from the FWF process")
plt.savefig(Filename_png)
plt.show()
plt.close()

