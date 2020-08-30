class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        result = 0
        for i in range(len(rows)):
            lookup = set(rows[i])
            for j in range(i):
                count = sum(1 for c in rows[j] if c in lookup)
                result += count*(count-1)/2
        return int(result)

val=Solution()
m=int(input())
matrix=[]
for i in range(m):
  rows=list(map(int,input().split()))
  matrix.append(rows)
print(val.countCornerRectangles(matrix))
