def numDivisor(n):
    '''
    n의 약수의 개수를 반환하는 함수를 작성하세요.
    '''
    sum_divisor = 0
    for i in range(1, n+1):
        if 0 == n % i:
            sum_divisor += 1
    return sum_divisor

def main():
    '''
    Do not change this code
    '''

    number = int(input())
    print(numDivisor(number))

if __name__ == "__main__":
    main()
