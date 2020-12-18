

def _get_char_counts(chars: str):
	char_counts = dict()
	
	for char in chars:  # initialize
		char_counts[char] = 0
			
	for char in chars:  # count occurances
		char_counts[char] += 1
		
	return char_counts
		
	

def only_unique_chars(chars: str):
	result = True
	
	char_map = _get_char_counts(chars)
		
	for key in char_map.keys():  # find more than 1 occurances
		if key != " " and char_map[key] > 1:
			result = False
			repeated = key
			break
			
	return result
	

def _only_unique_chars(chars: str):
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

