class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        coords = set()
        rows = len(board)
        cols = len(board[0])

        if rows == 1 and cols == 1 and len(word) == 1:
            return board[0][0] == word[0]


        def check_neighbors(coord, cur_str):
            r, c = coord

            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols):
                return False
            
            if cur_str == "":
                return True

            if coord in coords:
                return False

            if board[r][c] == cur_str[0]:
                coords.add(coord)
                found = (
                    check_neighbors((r - 1, c), cur_str[1:]) or
                    check_neighbors((r + 1, c), cur_str[1:]) or
                    check_neighbors((r, c - 1), cur_str[1:]) or
                    check_neighbors((r, c + 1), cur_str[1:])
                )
                coords.remove(coord)
                return found
            
            return False
        
        for r in range(rows):
            for c in range(cols):
                if check_neighbors((r,c), word):
                    return True
        
        return False
