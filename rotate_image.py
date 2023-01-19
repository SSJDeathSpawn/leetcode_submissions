def rotate_image(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])-1,-1,-1):
            line.append(matrix[j][i])
        new_matrix.append(line)
    matrix[:] = new_matrix


a = [[1,2,3],[4,5,6],[7,8,9]]
rotate_image(a)
print(a)
