def genome_length(s):
    # 구현해주세요!
    def init_cache(s, N):
        cache = [[-1] * (N+1) for _ in range(N+1)]
        for i in range(1, N):
            if (s[i] == 'a' and s[i + 1] == 't') or (s[i] == 'g' and s[i + 1] == 'c'):
                cache[i][i + 1] = 2;
            else:
                cache[i][i + 1] = 0;
        for i in range(1, N+1):
            cache[i][i] = 0;
        return cache
    
    def genome_length_helper(s, cache, i, j):
        ret = cache[i][j]
        if ret != -1:
            return ret

        max_length = -9999
        if (s[i] == 'a' and s[j] == 't') or (s[i] == 'g' and s[j] == 'c'):
            max_length = genome_length_helper(s, cache, i + 1, j - 1) + 2
            
        for k in range(i, j - 1 + 1):
            temp = genome_length_helper(s, cache, i, k)
            temp2 = genome_length_helper(s, cache, k + 1, j)
            temp += temp2
            max_length = max(temp, max_length)
        cache[i][j] = max_length

        return cache[i][j]
    
    N = len(s) - 1
    cache = init_cache(s, N)
    ans = genome_length_helper(s, cache, 1, N)

    return ans

def read_inputs():
    s = input().strip()
    # 편의상 0번째는 비워두고, 1번째 index부터 입력을 받습니다
    s = " "+s
    return s

def main():
    s = read_inputs()
    ans = genome_length(s)
    print(ans)

if __name__ == "__main__":
    main()