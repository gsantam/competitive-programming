class Solution:
    def perform_operation(self,token_1,token_2,op):
        if op=="+":
            return int(token_1)+int(token_2)
        if op=="-":
            return int(token_1)-int(token_2)
        if op=="*":
            return int(token_1)*int(token_2)
        if op=="/":
            return int(int(token_1)/int(token_2))

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+','-','*','/'):
                el_2 = stack.pop()
                el_1 = stack.pop()
                stack.append(self.perform_operation(el_1,el_2,t))
            else:
                stack.append(t)
        return int(stack[0])
