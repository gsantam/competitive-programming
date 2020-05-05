class Solution:
    def alienOrder(self, words: List[str]) -> str:
        bigger_than_me = dict()
        for word in words:
            for letter in word:
                bigger_than_me[letter] = set()
        one = False
        for i in range(1,len(words)):
            word_1 = words[i-1]
            word_2 = words[i]
            j = 0
            while j<min(len(word_1),len(word_2)):
                if word_1[j]!=word_2[j]:
                    bigger_than_me[word_2[j]].add(word_1[j])
                    one = True
                    break
                j+=1

        letters = ""
        stop = False
        initial_length = len(bigger_than_me)
        print(bigger_than_me)
        if len(bigger_than_me)==1:
            return list(bigger_than_me.keys())[0]
        if not one:
            return ""
        while len(bigger_than_me)>=2 and stop==False:
            current_letter = None
            for letter in bigger_than_me:
                if len(bigger_than_me[letter])==0:
                    if current_letter is None:
                        current_letter = letter
                    else:
                        stop =True
                        break
                    
            if current_letter is None:
                return ""
            
            letters+=current_letter
            for letter in bigger_than_me:
                if current_letter in bigger_than_me[letter]:
                    bigger_than_me[letter].remove(current_letter)
            del bigger_than_me[current_letter]
        print(bigger_than_me)
        if len(bigger_than_me)==initial_length:
            return ""

        for letter in bigger_than_me:
            letters+=letter
        return letters

