# Given two strings, write a method to decide if one is a permutation of the other.

# permutation: cats -> tacs


def check_permutation(this: str, that: str):
	"""
	O(n) runtime
	Compares two strings to see if they are permutations of each other.
	"""
	result = True
	this_char_counts = dict()
	
	for char in this:  # inititialize counts
		this_char_counts[char] = 0
			
	for char in this:  # perform counting
		this_char_counts[char] += 1
			
	for char in that:  # main iteration
		try:
			if this_char_counts[char] < 1:
				result = False
				break
			else:
				this_char_counts[char] -= 1
				
		except KeyError as ke:  # key was not found means the strings do not match
			result = False
			break
	
	return result
	
	
assert check_permutation("abc", "cba")
assert check_permutation("cats", "tacs")
assert check_permutation("state", "taste")
assert check_permutation("pass", "ssap")

print("All tests passing!")

