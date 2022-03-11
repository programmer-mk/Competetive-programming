class Solution:
    def is_valid_state(self, state, n):
        print(f'validating state: {state}')

        if len(state) != n * 2:
            return False
        open_count = 0
        for character in state:
            if character == ')':
                if open_count <= 0:
                    return False
                open_count -= 1
            elif character == '(':
                open_count += 1

        if open_count == 0:
            return True
        else:
            return False

    def get_candidates(self, state):
        return ['(', ')']

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            print(f'founded state: {state}')
            solutions.add("".join(state.copy()))

        if len(state) < n*2:
            state.append('(')
            self.search(state, solutions, n)
            state.pop()

            state.append(')')
            self.search(state, solutions, n)
            state.pop()

    def generateParenthesis(self, n: int):
        solutions = set()
        state = []
        self.search(state, solutions, n)
        return solutions