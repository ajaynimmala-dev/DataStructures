class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """check if the given matrix is valid or not"""
        i=0
        length_row=len(board[i])
        length_column=len(board)
        for row in range(0,length_row):
            for column in range(0,length_column):
                key=board[row][column]
                res1=row-row%3
                res2=column-column%3
                for search_row in range(res1,res1+3,1):
                    for search_column in range(res2,res2+3,1):
                        print("{}{}".format(search_row,search_column))
                        if board.index(board[search_row][search_column])==board.index
                        (board[row][column]) and key==board[search_row][search_column]:
                            print(False)
