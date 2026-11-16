class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #no duplicates in every sublist
        #no duplicates for every first element in every sublist
        #no duplicates for every 3, skip 6, range of 3 sublists
        #use dict to map numbers to how many times they appear, or check if it exists in the dictionary, if it does return False

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])

        return True
            

        

        

        