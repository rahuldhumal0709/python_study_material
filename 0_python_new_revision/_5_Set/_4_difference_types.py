set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

diff = set1.difference(set2) # diff = s1-s2
print('difference : ',diff) # {1, 2}

set1.difference_update(set2) # s1 = s1-s2
print("difference_update : ",set1) # {1, 2}
# ==============================================================
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sym_diff = set1.symmetric_difference(set2) # diff = (s1-s2) + (s2-s1)
print('symmetric_difference : ',sym_diff)  # Output: {1, 2, 5, 6}

set1.symmetric_difference_update(set2) # s1 = (s1-s2) + (s2-s1)
print('symmetric_difference_update : ',set1)  # Output: {1, 2, 5, 6}
