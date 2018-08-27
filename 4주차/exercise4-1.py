def lis(data):
    sequence = []
    
    #이곳에 문제 1에 대한 코드를 작성하세요.
    N = len(data)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo+hi)//2
            if (data[M[mid]] <= data[i]):
                lo = mid+1
            else:
                hi = mid-1
        
        newL = lo
        P[i] = M[newL-1]
        M[newL] = i

        if (newL > L):
            L = newL

    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(data[k])
        k = P[k]
    sequence = S[::-1]
    
    return sequence

def get_data():
    N = int(input())
    data = []
    for _ in range(N):
        tmp = [int(v) for v in input().split()]
        data.append(tmp)
    return data

if __name__ == '__main__':
    data = get_data()
    sorted_data = sorted(data)
    right_side_data = [v[1] for v in sorted_data]
    lis = lis(right_side_data)
    print (len(data) - len(lis))