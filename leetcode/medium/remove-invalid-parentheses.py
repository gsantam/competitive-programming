class Solution:
    
    def backtracking(self,current_s,i,open_removed,close_removed,n_open,n_close):
        if i == len(self.s):
            if open_removed==self.open_to_remove and close_removed == self.close_to_remove:
                self.all_combinations.add(current_s)
            return
        if self.s[i]=="(":
            if open_removed<self.open_to_remove:
                self.backtracking(current_s,i+1,open_removed+1,close_removed,n_open,n_close)
            if self.total_close-n_open-n_close>0: 
                self.backtracking(current_s+"(",i+1,open_removed,close_removed,n_open+1,n_close)
        elif self.s[i]==")":
            if close_removed<self.close_to_remove:
                self.backtracking(current_s,i+1,open_removed,close_removed+1,n_open,n_close)
            if n_open>0: 
                self.backtracking(current_s+")",i+1,open_removed,close_removed,n_open-1,n_close+1)      
        else:
            self.backtracking(current_s+self.s[i],i+1,open_removed,close_removed,n_open,n_close)
        

            
        
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.s = s
        self.total_close = len([char for char in s if char==")"])
        n_open = 0
        n_close = 0
        self.close_to_remove = 0
        self.open_to_remove = 0
        for i,char in enumerate(s):
            if char == ")":
                if n_open>0:
                    n_open-=1
                else:
                    self.close_to_remove+=1
                n_close+=1
                
            if char == "(":
                if self.total_close-n_open-n_close>0:
                    n_open+=1
                else:
                    self.open_to_remove+=1

        self.all_combinations = set()
        self.backtracking("",0,0,0,0,0)
        return list(self.all_combinations)
        
        
