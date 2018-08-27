def init_cache(s, N):
    # -1로 초기값을 설정한다
    cache = [[-1] * (N+1) for _ in range(N+1)]
    l_cache = [[-1] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N):
        if (s[i] == 'a' and s[i + 1] == 't') or (s[i] == 'g' and s[i + 1] == 'c'):
            cache[i][i + 1] = 2
        else:
            cache[i][i + 1] = 0

    for i in range(1, N+1):
        cache[i][i] = 0

    return cache, l_cache


def print_cache(cache, s, N):
    # 디버깅 목적으로 완성된 cache를 출력한다
    print("".rjust(8), end="")
    for i in range(1, N+1):
        print(str(i).rjust(4), end="")
    print("")
    print("".rjust(8), end="")
    for i in range(1, N+1):
        print(s[i].rjust(4), end="")
    print("")
    for i in range(1, N+1):
        print(str(i).rjust(4), end="")
        print(s[i].rjust(4), end="")
        for j in range(1, N+1):
            print(str(cache[i][j]).rjust(4), end="")
        print("")


def genome_length(s):    
    N = len(s) - 1
    cache, l_cache = init_cache(s, N)    
    ans = genome_length_helper(s, cache, l_cache, 1, N)
    genome = build_string(s, l_cache, 1, N)

    return ans, genome


def genome_length_helper(s, cache, l_cache, i, j):
    ret = cache[i][j]
    if ret != -1:
        return ret
    
    max_length = -9999
    if (s[i] == 'a' and s[j] == 't') or (s[i] == 'g' and s[j] == 'c'):
        max_length = genome_length_helper(s, cache, l_cache, i + 1, j - 1) + 2

    save_k = 0
    for k in range(i, j - 1 + 1):
        temp = genome_length_helper(s, cache, l_cache, i, k)
        temp2 = genome_length_helper(s, cache, l_cache, k + 1, j)
        temp += temp2
        if temp > max_length:
            max_length = temp
            save_k = k

    l_cache[i][j] = save_k
    cache[i][j] = max_length

    return cache[i][j]

def build_string(s, l_cache, i, j):
    if i+1 == j:
        if s[i]+s[j] == "at" or s[i]+s[j] == "gc":
            return s[i]+s[j]
    elif i >= j:
        return ""
    elif l_cache[i][j] == 0:
        return s[i] + build_string(s, l_cache, i+1, j-1) + s[j]
    else:
        return build_string(s, l_cache, i, l_cache[i][j]) + build_string(s, l_cache, l_cache[i][j]+1, j)

    return ""
    
def read_inputs():
    s = input().strip()
    # 편의상 0번째는 비워두고, 1번째 index부터 입력을 받습니다
    s = " "+s
    return s

def main():
    s = read_inputs()
    length, genome = genome_length(s)
    print(length, genome)

if __name__ == "__main__":
    main()