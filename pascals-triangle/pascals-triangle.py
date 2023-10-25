class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        for i in range(1, numRows):

            row = [1]

            for j in range(i-1):
                row.append(ans[-1][j] + ans[-1][j+1])

            row.append(1)
            ans.append(row)

        return ans





        