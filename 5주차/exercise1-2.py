def lcs_with_string(s1, s2):
    mat = [[0]*(len(s2)+1) for x in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    
    i = len(s1)
    j = len(s2)
    index = mat[i][j]

    lcs_str = [""] * index

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str[index-1] = s1[i-1]
            index = index - 1
            i = i - 1
            j = j - 1
            
        elif mat[i-1][j] > mat[i][j-1]:
            i = i - 1
        else:
            j = j - 1

    return mat[-1][-1], "".join(lcs_str)

def read_inputs():
    s1 = input().strip()
    s2 = input().strip()
    return s1, s2

def main():
    s1, s2 = read_inputs()
    ans = lcs_with_string(s1, s2)
    print(ans)

if __name__ == "__main__":
    main()