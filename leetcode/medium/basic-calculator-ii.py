class Solution:
    def calculate(self, s: str) -> int:
        s=s+"+"
        total = 0
        current_number = 0
        result_block = 0
        prev_operator = "+"
        for c in s:
            if c == " ":
                continue
            if c in ['+','-','/','*']:
                if prev_operator == '*':
                    result_block*=current_number
                elif prev_operator == '/':
                    result_block=int(result_block/current_number)
                elif prev_operator == '+':
                    result_block = current_number
                else:
                    result_block=-current_number
                if c in ['+','-']:
                    total+=result_block
                current_number = 0
                prev_operator = c
            else:
                current_number*=10
                current_number+=int(c)
        return total
