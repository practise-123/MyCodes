def shift_matrix(matrix, direction):
    if not matrix:
        return []

    num_rows, num_cols = len(matrix), len(matrix[0])

    if direction == 'up':
        for i in range(num_rows - 1):
            for j in range(num_cols):
                matrix[i][j] = matrix[i + 1][j]
        for j in range(num_cols):
            matrix[num_rows - 1][j] = 0

    elif direction == 'down':
        for i in range(num_rows - 1, 0, -1):
            for j in range(num_cols):
                matrix[i][j] = matrix[i - 1][j]
        for j in range(num_cols):
            matrix[0][j] = 0

    elif direction == 'left':
        for i in range(num_rows):
            for j in range(num_cols - 1):
                matrix[i][j] = matrix[i][j + 1]
            matrix[i][num_cols - 1] = 0

    elif direction == 'right':
        for i in range(num_rows):
            for j in range(num_cols - 1, 0, -1):
                matrix[i][j] = matrix[i][j - 1]
            matrix[i][0] = 0

    return matrix


# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
direction = 'left'
shifted_matrix = shift_matrix(matrix, direction)
for row in shifted_matrix:
    print(row)
