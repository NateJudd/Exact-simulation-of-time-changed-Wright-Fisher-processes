# Exact simulation of time changed Wright-Fisher processes
For fractional Wright-Fisher processes, s~E(t) is first simulated according to FengLin2023's (GitHub) code for the simulation of first passage times of subordinators. "Simulate_Subordinator_Inverse.py" imports his code and runs an example, which is then plotted and the data of simulated times written to ".csv". The simulated times are then plugged into the EWF exact sampler from JaroSant's (GitHub) code, see "Simulate_WF.py".

For subordinated Wright-Fisher processes, JaroSant's (GitHub) code is extended to include choices of Laplace transform other than the identity. The article \cite{} proves that the associated sampling scheme is exact. See the files "..", "..." and "...".
