class Solution:
    def toGoatLatin(self, S: str) -> str:
        goat_array = []
        if len(S)==0:
            return ""
        vowels = set(['a','e','i','o','u'])
        
        for i, word in enumerate(S.split(" ")):
            if word[0].lower() in vowels:
                word = word+"ma"
            else:
                word = word[1:]+word[0 ] + "ma"
            word = word + "a"*(i+1)
            goat_array.append(word) 
                
        return " ".join(goat_array)
        
