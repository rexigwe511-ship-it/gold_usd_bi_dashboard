import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. PARAMETERS
# -----------------------------
T = 800
p = 2
beta = -0.8
mu = 0.5
tau = 0.035

# Normal regime
alpha1 = 0.0
rho1 = -0.2
phi1 = -0.3
gamma1 = [0.2, 0.1]

# Crisis regime
alpha2 = 0.0
rho2 = -0.5
psi2 = 0.25
gamma2 = [0.1, 0.05]

np.random.seed(42)
sigma = 0.02

# -----------------------------
# 2. INITIALIZATION
# -----------------------------
G = np.zeros(T)
D = np.zeros(T)
G[0] = 7.7
D[0] = 4.5

# -----------------------------
# 3. SIMULATION
# -----------------------------
for t in range(2, T):
    # Dollar process (AR(1))
    D[t] = 0.9 * D[t-1] + 0.1 * np.random.randn()
    dD = D[t] - D[t-1]

    # Error correction term
    ECT = G[t-1] - (beta * D[t-1] + mu)

    # Regime switching
    if abs(ECT) <= tau:
        dG = (alpha1 +
              rho1 * ECT +
              phi1 * dD +
              gamma1[0] * (G[t-1] - G[t-2]) +
              gamma1[1] * (G[t-2] - G[t-3] if t > 2 else 0) +
              sigma * np.random.randn())
    else:
        dG = (alpha2 +
              rho2 * ECT +
              psi2 * dD +
              gamma2[0] * (G[t-1] - G[t-2]) +
              gamma2[1] * (G[t-2] - G[t-3] if t > 2 else 0) +
              sigma * np.random.randn())

    G[t] = G[t-1] + dG

# -----------------------------
# 4. PLOTTING
# -----------------------------
plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm"
})

plt.figure(figsize=(12, 6.75))
t = np.arange(T)

plt.plot(t, G, linewidth=2, label=r"$G_t$ (Gold)")
plt.plot(t, D, linewidth=2, label=r"$D_t$ (Dollar)")

plt.xlabel(r"$t$")
plt.ylabel(r"Values")
plt.title(r"TVECM Simulation: Gold--Dollar Dynamics with Crisis Regime (Hug)")
plt.legend()

plt.tight_layout()
plt.savefig("tvecm_simulation.png", dpi=300)
plt.show()
