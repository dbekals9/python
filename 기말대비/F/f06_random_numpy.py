#**random과 numpy 활용**  

import numpy as np
import random as rd

numbers = rd.sample(range(1, 46), 6)
arr = np.array(numbers)
print(numbers)
print(arr.mean())