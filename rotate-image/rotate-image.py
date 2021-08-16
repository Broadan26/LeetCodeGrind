class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        layer_count = len(matrix) // 2
        for layer in range(0, layer_count): #Iterate through rotating layers
            first = layer
            last = len(matrix) - first - 1
            for element in range(first, last): #Rotate each layer 90 degrees
                offset = element - first

                top = matrix[first][element] #Collect layer sides
                right_side = matrix[element][last]
                bottom = matrix[last][last - offset]
                left_side = matrix[last - offset][first]

                matrix[first][element] = left_side #Perform rotation
                matrix[element][last] = top
                matrix[last][last - offset] = right_side
                matrix[last - offset][first] = bottom
        return None