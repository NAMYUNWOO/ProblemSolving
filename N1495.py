import sys
sys.setrecursionlimit(100000)

DP = [[-2 for _ in range(1001)] for _ in range(101)]
N,S,M  = 0,0,0
V = []

def ans(i,p):
    if (p > M) or (p < 0):
        return -1
    if DP[i][p] != -2:
        return DP[i][p]
    if (i == N):
        return p
    DP[i][p] = max(ans(i+1,p+V[i]),ans(i+1,p-V[i]))
    return DP[i][p]
def main():
    global N,S,M,V
    N,S,M=(int(i.strip()) for i in input().split(" "))
    V = [int(i.strip()) for i in input().split(" ")]
    print(ans(0,S))
    return 0
main()