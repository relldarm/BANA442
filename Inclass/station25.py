import numpy as np

rng=np.random.default_rng(seed=4)

shows = rng.binomial(4, 0.85, size=100_000)
print((shows == 4).mean())