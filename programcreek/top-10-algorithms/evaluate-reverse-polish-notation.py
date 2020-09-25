# Recursivity

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = tokens
        operations = set(['+','-','*','/'])
        if len(symbols)==1:
            return int(symbols[0])
        for i,symbol in enumerate(symbols):
            if symbol in operations:
                if symbol=="+":
                    apply_symbol = int(symbols[i-1])+int(symbols[i-2])
                if symbol=="-":
                    apply_symbol = int(symbols[i-2]) - int(symbols[i-1])
                if symbol=="*":
                    apply_symbol = int(symbols[i-1])*int(symbols[i-2])
                if symbol=="/":
                    apply_symbol = int(int(symbols[i-2])/int(symbols[i-1]))

                return self.evalRPN(symbols[:i-2]+[str(apply_symbol)]+symbols[i+1:])
        
# Stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = tokens
        operations = set(['+','-','*','/'])
        stack = []
        current = None
        first = True
        if len(tokens)==1:
            return int(tokens[0])
        for i, symbol in enumerate(symbols[:]):
            if symbol in operations:
                n_1 = stack.pop()
                n_2 = stack.pop()

                if symbol=="+":
                    result = int(n_1)+int(n_2)
                if symbol=="-":
                    result = int(n_2)-int(n_1)
                if symbol=="*":
                    result = int(n_1)*int(n_2)
                if symbol=="/":
                    result = int(int(n_2)/int(n_1))

                current = result
                stack.append(result)
            else:
                stack.append(int(symbol))

        return current
        
