# 최대 구간 합 문제 (maximum subarray problem)

def read_data():
    array = [int(v) for v in input().split()]
    return array

def max_sum(array):
    l = len(array)
    m = int(l/2)
    if l == 1:
        return sum(array)
    array_l = array[:m]
    array_r = array[m:]
    answer = 1e-100

    # 이곳에 문제 3에 대한 코드를 작성하세요.
    m_l = max_sum(array_l)
    m_r = max_sum(array_r)
    m_m = in_between(array)
    answer = max(m_l, m_r, m_m)
    return answer

def in_between(array):
    l = len(array)
    m = int(l/2)
    array_l = array[:m][::-1]
    array_r = array[m:]
    m_l = stretch_array(array_l)
    m_r = stretch_array(array_r)
    return m_l + m_r

def stretch_array(array):
    cumsum = -1e100

    # 이곳에 문제 2에 대한 코드를 작성하세요.
    cumsum = -1e100
    for i in range(1, len(array) + 1):
        s = sum(array[:i])
        if s > cumsum:
            cumsum = s
    return cumsum

def main():
    array = read_data()
    print(in_between(array))

if __name__ == '__main__':
    main()