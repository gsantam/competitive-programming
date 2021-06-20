class Solution:
    def getMaxLength(self,words,current_words,used_letters):
        max_lenght = sum([len(word) for word in current_words])
        for i,word in enumerate(words):
            no_repetition = True
            for letter in word:
                if letter in used_letters:
                    no_repetition = False
                    break
            if no_repetition:
                current_words_ = current_words.copy()
                used_letters_ = used_letters.copy()
                current_words_.append(word)
                for letter in word:
                    used_letters_.add(letter)
                new_length = self.getMaxLength(words[i:],current_words_,used_letters_)
                if new_length>max_lenght:
                    max_lenght = new_length
        return max_lenght
            
    
    def maxLength(self, arr: List[str]) -> int:
        arr = [x for x in arr if len(set(x))==len(x)]
        return self.getMaxLength(arr,[],set())
        
        
