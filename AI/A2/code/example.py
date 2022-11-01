from itertools import permutations

import numpy as np

from factor import Factor
from vea import vea,normalize


# Define factors for the Bayesian network in a simplified version of the Holmes scenario (Lecture 9, slide 25)
f_MC = normalize(Factor(['MC'], np.array([0.8, 0.2])))
f_ISC = normalize(Factor(['MC','ISC'], np.array([[0.8, 0.2],[0.2,0.8]])))
f_B = normalize(Factor(['MC','B'], np.array([[0.95, 0.05],[0.8,0.2]])))
f_C = normalize(Factor(['B','ISC','C'], np.array([[[0.95,0.05],[0.2,0.8]],[[0.2,0.8],[0.2,0.8]]])))
f_SH = normalize(Factor(['B','SH'], np.array([[0.4, 0.6],[0.2,0.8]])))
f_CT = normalize(Factor(['B','CT'], np.array([[0.9, 0.1],[0.05,0.95]])))
# Execute VEA to answer the query P(B=True|A=False)
result, treewidth = vea([f_MC,f_ISC,f_B,f_C,f_SH,f_CT], ['B'], {'ISC': 1, 'SH':0}, ['MC','CT','C'], verbose=True)
print("\nP(B|A=False):\n")
print(result)
