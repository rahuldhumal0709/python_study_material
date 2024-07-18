dict1 = {'name': 'KL', 'age': 30}
dict2 = {'age': 32, 'city': 'Banglore'}

dict1.update(dict2)
print(dict1)  # Output: {'name': 'KL', 'age': 32, 'city': 'Banglore'}

# ===========================================================================

dict1.update([('age', 33), ('country', 'India')])
print(dict1)  # Output: {'name': 'KL', 'age': 33, 'city': 'Banglore', 'country': 'India'}

# ===========================================================================

dict1.update((('city', 'Mumbai'), ('jersey_number', '1')))
print(dict1)  # Output: {'name': 'KL', 'age': 33, 'city': 'Mumbai', 'country': 'India', 'jersey_number': '1'}

# ===========================================================================