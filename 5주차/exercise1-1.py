def lcs(s1, s2):
    # 구현해주세요!
    mat = [[0]*(len(s2)+1) for x in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])

    return mat[-1][-1]

def read_inputs():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2

def main():
    s1, s2 = read_inputs()
    ans = lcs(s1, s2)
    print(ans)

if __name__ == "__main__":
    main()