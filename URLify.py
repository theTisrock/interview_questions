# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string.

# NOTE: this is more challenging using a character array in Java AND perform the operation IN PLACE


# "Mr John Smith    "



def urlify(string: str):

	result = ""
	for char in string:
		result = result + "%20" if char == " " else result + char

	return result
	
	
	
assert urlify("hello world") == "hello%20world" 
assert urlify("a b") == "a%20b"
assert urlify("a b c") == "a%20b%20c"
assert urlify("a b c d") == "a%20b%20c%20d"

assert urlify("hi") == "hi"
assert urlify("") == ""

print("All tests passing!")
             
