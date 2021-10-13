# code here
import numpy as np
n_arr = np.array([75.523, 42.0, 65.32924763])
print("Given array:")
print(n_arr)
  
print("\nReplace all h are greater than 50. to 15.50")
n_arr[n_arr > 50.] = 15.50
  
print("New array :\n")
print(n_arr)
