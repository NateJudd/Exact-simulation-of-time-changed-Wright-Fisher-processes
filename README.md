
For subordinated Wright-Fisher processes, JaroSant's (GitHub) code is (here) extended to include choices of Laplace transform other than the identity. The article "Subordinated Wright-Fisher priors", available on ArXiv (at https://arxiv.org/abs/2604.1136), proves that the associated sampling scheme is exact. In this preprint you can also find plots produced from this code.


For fractional Wright-Fisher processes, s~E(t) is first simulated according to FengLin2023's (GitHub) code for the simulation of first passage times of subordinators. "Simulate_Subordinator_Inverse.py" imports his code and runs an example, which is then plotted and the data of simulated times written to ".csv". The simulated times are then plugged into the EWF exact sampler from JaroSant's scheme, see "Simulate_WF.py".

 ## Repository Structure

```text
.
├── README.md                     # Project documentation
├── LICENSE                       # MIT license
├── CMakeLists.txt                # Global build configuration
└── src/
    ├── CMakeLists.txt            # Module-specific build configuration
    ├── EWF_pybind.cpp            # Pybind11 interface
    ├── WrightFisher.cpp          # Wright-Fisher implementation
    ├── WrightFisher.h            # Wright-Fisher declarations
    ├── examples/
    │   ├── Simulate_Subordinator_Inverse.py  # Simulate inverse subordinator
    │   ├── FWF_sim.py                       # Simulate subordinated Wright-Fisher process
    │   └── tf_sim.py                        # Simulate Wright-Fisher process with subordinator clock
    └── utils/
        ├── merge_plots.R                    # Combine multiple plots into a single panel
        ├── plot_fwf.py                      # Plot subordinated Wright-Fisher trajectories
        └── print_overlapping_tf_dens.py     # Overlay multiple density curves
```
