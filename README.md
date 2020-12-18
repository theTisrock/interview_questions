# interview questions

I'll be using Python because of it's simplistic nature and it's ability to set up a sort of ad-hoc test suite with the "assert" keyword.

Implementations will be imperative in nature, even though python provides many utilities that enable using a more declarative approach. 



rabbit trail: Imperative vs Declarative

	Capitalizing a string -

		Imperative: (how some thing is done)
			Iterate through the string.
				Acquire the ASCII char code of the character.
				if the char code is within the range of a lowercase ASCII letter, convert it to uppercase by adding the proper interval according to ASCII chart
				convert the char code back to str form
				add char to result string
			return result string

		Declarative: (just supply the data)
			use Python's built-in .upper() method already attached to any string object.

