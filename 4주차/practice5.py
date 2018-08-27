import elice_utils

## wage: int list
## example: take_my_money([10, 20, 15, 25, 10, 20])
## return: int
def second_job(wage):
    #여기에 함수를 구현해 주세요.
    n = len(wage)
    wage = [0]+wage
    total = [0 for i in range(n+1)]

    for i in range(1, min(3,n)+1):
        if i!=3:
            total[i] = total[i-1] + wage[i]
        else:
            total[i] = max(wage[i]+total[i-2], wage[i]+wage[i-1])
    for i in range(4, n+1):
        total[i] = max(wage[i] + total[i-2], wage[i]+wage[i-1]+total[i-3])
    return total[n]

def main():
    N = int(input())
    wage = []
    for n in range(N):
        wage.append(int(input()))
        # 함수 호출과 출력을 위한 부분입니다. 수정하지 마세요.
        print(second_job(wage))
    
if __name__ == "__main__":
    main()
