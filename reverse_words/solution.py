class Solution:
    def reverseWords(self, s: str) -> str:
        divided_string = s.split()  
        divided_string = divided_string[::-1]  
        return " ".join(divided_string) 