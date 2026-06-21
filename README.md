
For subordinated Wright-Fisher processes, JaroSant's (GitHub) code is (here) extended to include choices of Laplace transform other than the identity. The article "Subordinated Wright-Fisher priors", available on ArXiv (at https://arxiv.org/abs/2604.1136), proves that the associated sampling scheme is exact. In this preprint you can also find plots produced from this code.


For fractional Wright-Fisher processes, s~E(t) is first simulated according to FengLin2023's (GitHub) code for the simulation of first passage times of subordinators. "Simulate_Subordinator_Inverse.py" imports his code and runs an example, which is then plotted and the data of simulated times written to ".csv". The simulated times are then plugged into the EWF exact sampler from JaroSant's scheme, see "Simulate_WF.py".



├── README.md         # read me file
├── LICENSE               # MIT licence
├── CMakeLists.txt     # global parameters
└── src/
    ├── CMakeLists.txt      # local (module) parameters
    ├── EWF_pybind.cpp   # pybind c++
    ├── WrightFisher.cpp   # sWF functions c++
    ├── WrightFisher.h       # sWF functions c++

└── examples/
    ├── Simulate_Subordinator_Inverse.py # simulate subordinator inverse
    ├── FWF_sim.py                                       # simulate sWF with inverse subordinator clock
    ├── tf_sim.py                                            # simulate sWF with subordinator clock
    
└── utils/
    ├──  merge_plots.R                          # script to combine multiple plots into a single panel
    ├──  plot_fwf.py                                # script to plot the sWF with subordinator inverse clock
    ├──  print_overlapping_tf_dens.py # script to combine multiple density curves onto a single plot

