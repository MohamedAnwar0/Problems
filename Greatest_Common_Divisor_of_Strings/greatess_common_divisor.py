word1 = input('Enter the first word')
word2 = input('Enter the second word')

result = ''

if (word1+word2 == word2+word1):
	
	length_substring = gcd(len(word1), len(word2))
        return str1[0:length_substring]
return ""
