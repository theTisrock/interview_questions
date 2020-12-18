#
# Implement an algorithm to determine if a string has all unique characters.
# What is you cannot use additional data structures?


def only_unique_chars(chars: str):
	"""
	O(n) runtime
	Uses a hash map as a helper to count char occurences.
	"""
	result = True
	char_counts = dict()
	
	for char in chars:  # initialize
		if char != " ":
			char_counts[char] = 0
			
	for char in chars:  # count occurances
		if char != " ":
			char_counts[char] += 1
		
	for key in char_counts.keys():  # find more than 1 occurances
		if char_counts[key] > 1:
			result = False
			repeated = key
			break
			
	return result
	

def _only_unique_chars(chars: str):
	"""
	O(n^2) runtime
	Uses no additional data structures. Instead, it compares each char to every other char to find a duplicate case.
	"""
	result = True
	
	start_at = 0
	for char in chars:
		if char != " ":
			start_at += 1
			for i in range(start_at, len(chars)):
				if char == chars[i]:
					result = False
					break
				
	return result
		
				
		
	
	
	
assert only_unique_chars("a") is True
assert only_unique_chars("ab") is True
assert only_unique_chars("aba") is False

assert _only_unique_chars("a") is True
assert _only_unique_chars("ab") is True
assert _only_unique_chars("aba") is False

assert only_unique_chars("abcdefghijklmnopqrstuvwxyz") is True
assert _only_unique_chars("abcdefghijklmnopqrstuvwxyz") is True

print("Success!")

