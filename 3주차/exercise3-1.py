# 최대 구간 합 문제 (maximum subarray problem)

def read_data():
    array = [int(v) for v in input().split()]
    return array

def max_sum(array): 
    m = -1e100
    l = len(array)

    # 이곳에 문제 1에 대한 코드를 작성하세요.
    m = -1e100
    l = len(array)
    for x in range(l):
        for y in range(x+1, l+1):
            s = sum(array[x:y])
            if m < s:
                m = s
    return m

def main():
    array = read_data()
    print(max_sum(array))

if __name__ == '__main__':
    main()