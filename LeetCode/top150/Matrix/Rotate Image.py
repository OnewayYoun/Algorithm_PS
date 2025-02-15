from typing import List


class Solution:
    """
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(map(list, zip(*matrix[::-1])))
        print(matrix)


Solution().rotate(matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
)
