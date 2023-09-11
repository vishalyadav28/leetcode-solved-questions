class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #solution 1

        # def make_row(i):
        #     for j in range(len(matrix)):
        #         if matrix[i][j]!=0:
        #             matrix[i][j] = -1
            
        # def make_col(j):
        #     for i in range(len(matrix)):
        #         if matrix[i][j]!=0:
        #             matrix[i][j] = -1


        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 0:
        #             make_row(i)
        #             make_col(j)

        # #now make it zero

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == -1:
        #             matrix[i][j] = 0

        # return matrix

        # solution 2
        n = len(matrix)
        m = len(matrix[0])
        rows = n * [0]
        cols = m * [0]
        for i in range(n):
                for j in range(m):
                    if matrix[i][j] == 0:
                        rows[i] = 1
                        cols[j] = 1
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

        return matrix



        
