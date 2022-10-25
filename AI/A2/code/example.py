from itertools import permutations

import numpy as np

from factor import Factor
from vea import vea


# Define factors for the Bayesian network in a simplified version of the Holmes scenario (Lecture 9, slide 25)
f_B = Factor(['B'], np.array([0.7, 0.3]))
f_E = Factor(['E'], np.array([0.9, 0.1]))
f_A = Factor(['B', 'E', 'A'], np.array([[[0.9, 0.1], [0.8, 0.2]], [[0.3, 0.7], [0.2, 0.8]]]))
f_W = Factor(['A', 'W'], np.array([[0.6, 0.4], [0.2, 0.8]]))

# Execute VEA to answer the query P(B=True|A=False)
result, treewidth = vea([f_E, f_B, f_A, f_W], ['B'], {'A': 0}, ['W', 'E'], verbose=True)
print("\nP(B|A=False):\n")
print(result)
