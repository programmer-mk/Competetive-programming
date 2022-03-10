class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result

        for i in range(1,numRows):
            elem_list = [1]
            for j in range(i-1):
                elem_list.append(result[i-1][j] + result[i-1][j+1])
            elem_list.append(1)
            result.append(elem_list)

        return result