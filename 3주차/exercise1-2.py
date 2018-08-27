def find_max_area(choco_width, heights):
    # 구현해 주세요!
    return find_max_area_helper(heights, 0, choco_width-1)

def find_max_area_helper(h, left, right):
    # Base Case: 초콜렛 너비가 1일 때
    if left == right:
        return h[left]

    # 두 구간을 분할하여 각각 풀기
    mid = int((left + right) / 2)
    ret = max(find_max_area_helper(h, left, mid), find_max_area_helper(h, mid + 1, right))

    # 중간에 겹치는 부분 구하기
    lo = mid
    hi = mid + 1
    height = min(h[lo], h[hi])
    ret = max(ret, height * 2)

    # 중간에서 시작해서 입력을 다 덮을 때까지 키운다
    while left < lo or hi < right:
        # 항상 높이가 더 높은 쪽으로 확장한다
        if hi < right and (lo == left or h[lo - 1] < h[hi + 1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1 
            height = min(height, h[lo])
        # 확장한 후 넓이를 다시 갱신한다
        ret = max(ret, height * (hi - lo + 1))

    return ret


def read_inputs():
    num_testcases = int(input())
    testcases = []
    for i in range(num_testcases):
        choco_width = int(input())
        heights = [int(x) for x in input().split()]
        testcases.append((choco_width, heights))

    return testcases

def main():
    testcases = read_inputs()
    for choco_width, heights in testcases:
        ans = find_max_area(choco_width, heights)
        print(ans)

if __name__ == "__main__":
    main()