import elice_utils

## wage: int list
## example: third_job([10, 20, 15, 25, 10, 20])
## return: int
def third_job(wage):
    #여기에 함수를 구현해 주세요.
    n = len(wage)
    wage = [0] + wage
    total = [0 for i in range(n+1)]
    path = [0 for i in range(n+1)]
    total[1] = wage[1]
    total[2] = wage[1] + wage[2]
    path[1] = 0
    path[2] = 2
    for i in range(3, min(3,n)+1):
        if 3 != i:
            total[i] = total[i-1] + wage[i]
            path[i] = i - 1
        else:
            t1 = wage[i-1]
            t2 = total[i-2]
            if t1 > t2:
                total[i] = wage[i] + t1
                path[i] = 2
            else:
                total[i] = wage[i] + t2
                path[i] = 1
    for i in range(4, n+1):
        t1 = wage[i-1] + total[i-3]
        t2 = total[i-2]
        if t1 > t2:
            total[i] = wage[i] + t1
            path[i] = 2
        else:
            total[i] = wage[i] + t2
            path[i] = 1
    max_path = []
    i = n
    while i > 0:
        max_path.append(i)
        if path[i] == 1:
            i -= 2
        else:
            if i > 1:
                max_path.append(i-1)
            i -= 3
    return max_path[::-1]

def main():
    N = int(input())
    wage = []
    for n in range(N):
        wage.append(int(input()))
        # 함수 호출과 출력을 위한 부분입니다. 수정하지 마세요.
    print(third_job(wage))
    
if __name__ == "__main__":
    main()
