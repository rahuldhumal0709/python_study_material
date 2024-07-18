set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

# Check if set1 and set2 are disjoint
print(set1.isdisjoint(set2))  # Output: True
# It returns True because there are no common elements between set1 and set2.

# Check if set1 and set3 are disjoint
print(set1.isdisjoint(set3))  # Output: False
# It returns False because set1 and set3 both contain the element 3

empty_set = set()
non_empty_set = {1, 2, 3}

# Check if an empty set and a non-empty set are disjoint
print(empty_set.isdisjoint(non_empty_set))  # Output: True
# It returns True because an empty set is considered disjoint with any set.