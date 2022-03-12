class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board[0])
        M = len(board)
        WORD_SIZE = len(word)
        visited = [[False for _ in board[0]] for _ in board]

        def dfs(r, c, next_index) -> bool:
            if next_index == WORD_SIZE:
                return True

            if r < 0 or r > M - 1 or c < 0 or c > N - 1:
                return False

            if visited[r][c] or word[next_index] != board[r][c]:
                return False

            visited[r][c] = True
            result = dfs(r-1, c, next_index+1) or dfs(r+1, c, next_index+1) or \
                     dfs(r, c-1, next_index+1) or dfs(r, c+1, next_index+1)

            visited[r][c] = False
            return result

        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True
        return False