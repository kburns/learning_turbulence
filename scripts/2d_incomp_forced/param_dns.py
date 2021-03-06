"""Parameters file."""

import numpy as np

# Domain
L = 2 * np.pi
N = 4096
mesh = None

# Stochastic forcing
ε = 1  # Energy injection rate
kf = 100  # Forcing wavenumber
kfw = 2  # Forcing width
seed = None

# Physical parameters
# Prescribed
lν_kmax = 3  # Enstrophy dissipation scale
lα = L  # Friction scale
# Derived
kmax = N * np.pi / L
lν = lν_kmax / kmax
η = ε * kf**2
ν = lν**2 * η**(1/3)
α = ε**(1/3) * lα**(-2/3)

# Temporal parameters
dx = L / N
Uα = ε**(1/3) * lα**(1/3)
safety = 0.5
dt = safety * dx / Uα
ts = "RK443"
stop_sim_time = np.inf
stop_wall_time = np.inf
scalars_iter = 10
snapshots_iter = 100
stop_iteration = 100000

