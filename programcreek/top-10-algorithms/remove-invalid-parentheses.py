class Solution:
    def recurrence(self,pos,current,open_removed,close_removed,n_open,n_close):
        if pos == len(self.s):
            if open_removed==self.open_to_remove and close_removed==self.close_to_remove :
                self.combinations.add(current)
            return 
        
        current_char = self.s[pos]
        if current_char!="(" and current_char!=")":
            self.recurrence(pos+1,current+current_char,open_removed,close_removed,n_open,n_close)
        
        elif current_char == "(":
            if self.total_close - n_close - (self.close_to_remove - close_removed) > 0:
                self.recurrence(pos+1,current+current_char,open_removed,close_removed,n_open+1,n_close)
            
            if open_removed < self.open_to_remove:
                self.recurrence(pos+1,current,open_removed +1,close_removed,n_open,n_close)
            
        elif current_char == ")":
            
            if n_open - n_close > 0:            
                self.recurrence(pos+1,current+current_char,open_removed,close_removed,n_open,n_close+1)
            
            if close_removed < self.close_to_remove:
                self.recurrence(pos+1,current,open_removed ,close_removed+1,n_open,n_close)

        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.close_to_remove = 0
        self.open_to_remove = 0
        self.total_close = len([char for char in s if char==")"])
        n_opened = 0
        close_seen = 0
        
        for char in s:
            if char!="(" and char!=")":
                continue
            if char == "(":
                if self.total_close - close_seen - n_opened>0:
                    n_opened+=1
                else:
                    self.open_to_remove+=1
                    
            if char == ")":
                close_seen+=1
                if n_opened>0:
                    n_opened-=1
                else:
                    self.close_to_remove+=1
        
        self.s = s
        self.combinations = set()
        self.recurrence(0,"",0,0,0,0)
        
        return list(self.combinations)
        
