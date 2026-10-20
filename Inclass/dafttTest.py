import numpy as np
rng = np.random.default_rng(seed=5)
n = 100_000

theta = rng.uniform(0.05, 0.09, size=n)   # parent first
x = rng.binomial(1, theta)              # child second, one x per theta
print(x.mean())                         # ~0.55, the middle of theta's range