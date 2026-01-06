class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n_ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    if i>=1 and board[i-1][j]=='X':
                        continue
                    if j>=1 and board[i][j-1]=='X':
                        continue
                    n_ships+=1
        return n_ships

