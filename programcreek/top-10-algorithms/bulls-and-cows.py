class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls =0
        cows = 0
        count_secret = {}
        count_guess = {}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                if secret[i] not in count_secret:
                    count_secret[secret[i]]=0
                count_secret[secret[i]]+=1
                
                if guess[i] not in count_guess:
                    count_guess[guess[i]]=0
                count_guess[guess[i]]+=1
        
        for letter in count_guess:
            if letter in  count_secret:
                cows+=min(count_secret[letter],count_guess[letter])

        return str(bulls) + "A" + str(cows)+"B"
        
        
