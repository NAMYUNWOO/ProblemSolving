import numpy as np

def create_table(a, b, c):
    table = np.zeros((len(a) + 1, len(b) + 1, len(c) + 1))

    # 여기에 문제 2에 대한 코드를 작성하세요.
    # 문제 1에 대한 코드를 대칭성을 생각하면서 확장시키면 됩니다. 
    for idx_a, aa in enumerate(a):
        for idx_b, bb in enumerate(b):
            for idx_c, cc in enumerate(c):
                if aa == bb and bb == cc:
                    table[idx_a + 1, idx_b + 1, idx_c + 1] = table[idx_a, idx_b, idx_c] + 1
                else:
                    table[idx_a + 1, idx_b + 1, idx_c + 1] = max(
                        table[idx_a + 1, idx_b + 1, idx_c],
                        table[idx_a + 1, idx_b, idx_c + 1],
                        table[idx_a, idx_b + 1, idx_c + 1],
                    )
    return table

def lcs(a, b, c):
    table = create_table(a, b, c)
    
    result = ""
    idx_a, idx_b, idx_c = len(a), len(b), len(c)
    while idx_a != 0 and idx_b != 0 and idx_c != 0:
        # 여기에 문제 2에 대한 코드를 작성하세요.
        if table[idx_a][idx_b][idx_c] == table[idx_a-1][idx_b][idx_c]:
            idx_a -= 1
        elif table[idx_a][idx_b][idx_c] == table[idx_a][idx_b-1][idx_c]:
            idx_b -= 1
        elif table[idx_a][idx_b][idx_c] == table[idx_a][idx_b][idx_c-1]:
            idx_c -= 1
        else:
            result = a[idx_a-1] + result
            idx_a -= 1
            idx_b -= 1
            idx_c -= 1
    return result

def read_input():
    a = input(); b = input(); c = input()
    a = [v for v in a]; b = [v for v in b]; c = [v for v in c]
    return [a, b, c]

def main():
    a, b, c = read_input()
    answer = lcs(a, b, c)
    print (len(answer))

if __name__ == '__main__':
    main()