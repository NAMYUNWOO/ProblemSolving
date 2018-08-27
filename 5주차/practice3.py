def sum_of_third_powers_student(N):
    """
    박재석 분의 코드
    """
    cubesumarr = [0] * (N+1)
    cubearr = list()
    for i in range(1, N):
        cube = i ** 3
        if cube <= N:
            cubearr.append(cube)
        else:
            break

    cubesumarr[0] = 0
    cubesumarr[1] = 1
    for k in range(2, N+1):
        cubesumarr[k] = min([cubesumarr[k - cubenum] for cubenum in cubearr if cubenum <= k ]) + 1
        
    return cubesumarr[-1]

def sum_of_third_powers_TA(N):
    count = [0] * (N + 1)
    for i in range(1, N + 1):
        n = 1
        min = N + 1
        while i - n ** 3 >= 0:
            if min > count[i - n ** 3] + 1:
                count[i] = count[i - n ** 3] + 1
                min = count[i]
            n += 1
    return count[N]

def main():
    # 입력
    N = int(input())
    # 출력
    print(sum_of_third_powers(N))

if __name__ == "__main__":
    main()
