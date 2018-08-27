def Solution(n):
    '''
    여기에 Solution 함수를 구현하세요
    '''
    comb = [0 for i in range(n + 1)]

	comb[0] = 1
    comb[1] = 1
    for i in range(2, n + 1):
        comb[i] = comb[i - 1] + 2 * comb[i - 2]

	return comb[n]

def main():
    T = int(input())

    for testcase in range(T):
        n = int(input())
        print(Solution(n))

if __name__ == "__main__":
    main()
