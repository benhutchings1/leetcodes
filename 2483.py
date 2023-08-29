import numpy as np

#
# Leetcode problem 2483 
# Minimum Penalty For a Shop
#
def bestClosingTime(customers: str) -> int:
    # Initialise penalties
    penalties = [0] * (len(customers) + 1)
    # Iterate over all operating times
    for i, stat in enumerate(customers):
        # Change penalties for an arrival
        if stat == "Y":
            for j in range(i+1):
                penalties[j] += 1
        else:
            # Change penalties for no arrival
            for j in range(i+1, len(customers)+1):
                penalties[j] += 1
    # Return earliest possible lowest penalty
    return np.argmin(penalties)

assert bestClosingTime("YYNY") == 2
assert bestClosingTime("YYYY") == 4
assert bestClosingTime("NNNN") == 0