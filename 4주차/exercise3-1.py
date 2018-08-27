import numpy as np

def create_table(a, b):
    table = np.zeros((len(a) + 1, len(b) + 1))

    # 여기에 문제 1에 대한 코드를 작성하세요.
    # table 의 가로, 세로 길이는 주어진 문자열의 길이보다 1이 크다는 것을 유념하세요.
    for idx_a, aa in enumerate(a):
        for idx_b, bb in enumerate(b):
            if aa == bb:
                table[idx_a + 1, idx_b + 1] = table[idx_a, idx_b] + 1
            else:
                table[idx_a + 1, idx_b + 1] = max(table[idx_a + 1, idx_b], table[idx_a, idx_b + 1])
    
    return table

def lcs(a, b):
    table = create_table(a, b)

    result = ""
    idx_a, idx_b = len(a), len(b)
    while idx_a != 0 and idx_b != 0:
        # 여기에 문제 1에 대한 코드를 작성하세요.
        # 가장 a, b 의 가장 끝 문자열 부터 시작해서 역으로 시작 문자열 까지 탐색해 나가는 방식입니다.
        if table[idx_a][idx_b] == table[idx_a-1][idx_b]:
            idx_a -= 1
        elif table[idx_a][idx_b] == table[idx_a][idx_b-1]:
            idx_b -= 1
        else:
            assert a[idx_a-1] == b[idx_b-1]
            result = a[idx_a-1] + result
            idx_a -= 1
            idx_b -= 1
    return result

def read_input():
    a = input(); b = input()
    a = [v for v in a]; b = [v for v in b]
    return [a, b]

def main():
    a, b = read_input()
    answer = lcs(a, b)
    print (len(answer))

if __name__ == '__main__':
    main()