
def saddle_point(matrix):
    l_min = None
    y = 0
    l_index = None

    if len(matrix) == 1:
        return 0, 0

    while len(matrix) > y:
        for i in matrix:
            l_min = min(i)
            l_index = i.index(l_min)
            for j in matrix:
                if l_min > j[l_index]:
                    return matrix.index(i), l_index
        return False


if __name__ == '__main__':
    print(saddle_point([[1,2,3],[3,2,1]]))
    print(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]))
    print(saddle_point([[21]]))