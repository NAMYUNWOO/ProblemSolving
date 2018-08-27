def palindrome(s):
    l = len(s)
    dp = [[0 for i in range(l)] for j in range(l)]
    for i in range(len(s)-1,-1,-1):
        for j in range(i,len(s)):
            if i==j: dp[i][j] = 1
            elif j-1==i and s[i]==s[j]: dp[i][j] = 1
            elif dp[i+1][j-1]==1 and s[i]==s[j]: dp[i][j] = 1

    index = 0
    for i in range(len(s)):
        if dp[i][len(s)-1]==1:
            index = i
            break

    answer = len(s) + index

    return (answer)

def get_data():
    data_list = []
    N = int(input())
    for _ in range(N):
        d = input()
        data_list.append(d)
    return (data_list)

def main():
    data = get_data()
    ans_list = []
    for d in data:
        palin_len = palindrome(d)
        ans_list.append(palin_len)
    print (ans_list)

if __name__ == "__main__":
    main()
