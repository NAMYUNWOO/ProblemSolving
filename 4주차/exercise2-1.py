def find_combi(n, r):
    # (1~30)C(1~30)까지의 모든 조합을 DP로 구하여 저장합니다.
    cache = build_combi_cache(30)
    # nCr을 리턴합니다.
    return cache[n][r]

def build_combi_cache(upper_limit):
    # (1~30)C(1~30)까지의 모든 조합을 DP로 구합니다.
    cache = []
    # 이치원 배열을 만듭니다.
    for n in range(upper_limit):
        arr = [0 for i in range(0, upper_limit+1)]
        cache.append(arr)
    # 1C1부터 시작하면서 조합 cache를 채웁니다.
    for n in range(1,upper_limit):
        for r in range(1, n+1):
            # (1~30)C1 라인에는 1..30이 들어갑니다.
            if r == 1:
                cache[n][r] = n
            # 1C1, 2C2, 3C3 ... 대각선 줄에는 n이 들어갑니다.
            elif n == r:
                cache[n][r] = 1
            # 그 외의 조합은 바로 전에 구한 조합들을 합하여 계산합니다:
            else:
                cache[n][r] = cache[n-1][r-1] + cache[n-1][r]
    return cache
    
def read_inputs():
    num_testcases = int(input())
    testcases = []
    for i in range(num_testcases):
        line = [int(x) for x in input().split()]
        r = line[0]
        n = line[1]
        testcases.append((n, r))

    return num_testcases, testcases

def main():
    num_testcases, testcases = read_inputs()
    for n, r in testcases:
        ans = find_combi(n, r)
        print(ans)

if __name__ == "__main__":
    main()