class Solution:
    def sorted_lex(self,n,current):
        if current>n:
            return
        if current!=0:
            self.all_numbers.append(current)
        for i in range(0,10):
            if current*10+i!=0:
                self.sorted_lex(n,current*10+i)

    def lexicalOrder(self, n: int) -> List[int]:
        self.all_numbers = []
        self.sorted_lex(n,0)
        return self.all_numbers
        
