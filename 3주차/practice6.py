import numpy as np
import sys
sys.setrecursionlimit(1000001)
LIMIT_NUMBER = 10007


def squaring_mat(mat, n):
    #implement here...
    if n < 0: 
        return "Invalid Input"
    elif n == 0:
         return np.eye(np.shape(mat)[0])
    elif n == 1:
        return mat
    elif n % 2 == 0:
        return squaring_mat(np.dot(mat, mat) % LIMIT_NUMBER, n/2) 
    else:
        return np.dot( mat, squaring_mat(np.dot(mat, mat) % LIMIT_NUMBER, (n-1)/2)) % LIMIT_NUMBER





    return


def linear_mat_multiple(mat, n):
    '''
    Refer this function while writing sqaring_mat(mat, n).
    '''

    if n == 1:
        return mat
    else:
        return np.dot(mat, linear_mat_multiple(mat, n-1)) % LIMIT_NUMBER

def get_input():
    '''
    Do not change this code.
    '''
    n_of_cases = int(input())
    
    cases = []
    for c in range(n_of_cases):
        m, n = [int(x) for x in input().strip().split(' ')]

        matrix = []
        for i in range(m):
            row = [int(x) for x in input().strip().split(' ')]
            matrix.append(row)
        matrix = np.array(matrix)
        cases.append((matrix, n))

    return cases

def main():
    '''
    Do not change this code.
    '''
    cases = get_input()
    for case in cases:
        mat, n = case
        result = squaring_mat(mat, n)
        print(result)

    return

if __name__ == '__main__':
    main()