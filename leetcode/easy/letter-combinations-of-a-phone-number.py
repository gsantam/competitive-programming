class Solution:
    def helper(self,i,digits,seq):
        if i==len(digits):
            self.total.append(seq)
            return
        
        digit = digits[i]
        for letter in self.my_dict[digit]:
            seq_ = seq+letter
            self.helper(i+1,digits,seq_)
            
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        self.total = []
        self.helper(0,digits,"")
        return self.total
        
        
