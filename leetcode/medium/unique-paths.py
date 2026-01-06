class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n_ways = [[0 for i in range(n+1)] for j in range(m+1)]
        n_ways[1][1] = 1
        for i in range(1,max(m,n)+1):
            for j in range(1,max(m,n)+1):
                if i==j:
                    break
                if i<=m and j<=n:
                    n_ways[i][j] += n_ways[i][j-1] + n_ways[i-1][j]
                if i<=n and j<=m:
                    n_ways[j][i] += n_ways[j][i-1] + n_ways[j-1][i]
            if i<=n and i<=m:
                n_ways[i][i] += n_ways[i-1][i] + n_ways[i][i-1]
        return n_ways[m][n]
