def repeating_letter_check(stringOfLetters):
	letterDictionary = []
	if stringOfLetters:
		for value in stringOfLetters:
			letterDictionary.append(value)
	return len(set(letterDictionary))==len(stringOfLetters)

def repeating_letter_check_fast(stringOfLetters):
	letterDictionary = []
	if stringOfLetters:
		for value in stringOfLetters:
			if (value in letterDictionary):
				return false
			letterDictionary.append(value)
	else return False
	return True


def find_repeating_letter_check(stringOfLetters):
	letterDictionary = {}
	if stringOfLetters:
		for value in lenstringOfLetters:
			if letterDictionary[value]:
				return letterDictionary[value]
			letterDictionary[value]=value

print(find_repeating_letter_check("hello"))
print(find_repeating_letter_check("helo"))
