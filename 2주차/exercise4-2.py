import numpy as np

def visit_all_nodes(shape):
    n = 0
    return_this = []

    column_start = 0; column_end = shape[1]
    row_start = 0; row_end = shape[0]

    while (len(return_this) != np.prod(shape)):
        if n % 4 == 0:
            for j in range(column_start, column_end):
                return_this.append((row_start, j))
            row_start += 1
        elif n % 4 == 1:
            for i in range(row_start, row_end):
                return_this.append((i, column_end - 1))
            column_end -= 1
        elif n % 4 == 2:
            for j in range(column_start, column_end)[::-1]:
                return_this.append((row_end - 1, j))
            row_end -= 1
        else:
            for i in range(row_start, row_end)[::-1]:
                return_this.append((i, column_start))
            column_start += 1
        n += 1

    return return_this

def return_outerair(matrix):
    outerair = set()

    # 이곳에 문제 1에 대한 코드를 작성하세요.
    shape = matrix.shape
    while True:
        cnt_prev = len(outerair)
        for node in visit_all_nodes(shape):
            nodes_around = lookaround(node)
            if matrix[node[0]][node[1]] == 1:
                continue
            if ((0 in node) or node[0] == shape[0] - 1 or node[1] == shape[1] - 1):
                outerair.add(node)
            else:
                if len(set(nodes_around) & outerair) != 0:
                    outerair.add(node)
        cnt_now = len(outerair)
        if cnt_now == cnt_prev:
            break
    return (outerair)

def return_contacted_sugar(matrix, outerair):
    contacted_sugar = []
    for node in visit_all_nodes(matrix.shape):
        nodes_around = lookaround(node)
        if matrix[node] == 1 and len(set(nodes_around) & set(outerair)) != 0:
            contacted_sugar.append(node)

    return (contacted_sugar)

def remove_nodes(matrix):
    return_matrix = matrix.copy()
    outerair = return_outerair(matrix)
    will_be_removed = return_contacted_sugar(matrix, outerair)

    # 이곳의 코드를 작성하여 문제 2를 푸세요.
    for node in will_be_removed:
        return_matrix[node] = 0
    return return_matrix

def lookaround(node):
    returnthis = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i + j) == 1:
                returnthis.append((node[0] + i, node[1] +j))
    return returnthis

def read_input():
    dimension = tuple([int(v) for v in input().split()])
    given_data = np.zeros(dimension).astype(int)
    for i in range(dimension[0]):
        row = [int(v) for v in input().split()]
        given_data[i] = row
    return given_data

def main():
    given_matrix = read_input()
    print (return_outerair(given_matrix))

if __name__ == "__main__":
     main()
