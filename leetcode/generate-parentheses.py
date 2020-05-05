class Solution:
    def recursion_parentesis(self,total,n_open,n_close,sequence):
        seq_total = []
        if len(sequence) == total*2:
            return [sequence]
        if n_open<total:
            seq_1 = self.recursion_parentesis(total,n_open+1,n_close,sequence+"(")
            seq_total+=seq_1
        if n_open - n_close>0:
            seq_2 = self.recursion_parentesis(total,n_open,n_close+1,sequence+")")
            seq_total+=seq_2

        return seq_total
        
    def generateParenthesis(self, n):
        seq_total = self.recursion_parentesis(n,0,0,"")
        return seq_total        
        
