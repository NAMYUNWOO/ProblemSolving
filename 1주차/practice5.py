import elice_utils

def binarySearch(array, value, low, high):
    '''
    array의 [low, high] 내에 value가 존재하면 True를, 존재하지 않으면   False를 반환합니다.
    '''
    if low > high:
        return False
    mid = (low+high) // 2
    if array[mid] > value:
        return binarySearch(array, value, low, mid-1)
    elif array[mid] < value:
        return binarySearch(array, value, mid+1, high)
    else:
        return True
    return False

def main():
    '''
    Do not change this code
    '''
    array_len = int(input())
    array = [int(x) for x in input().strip().split(" ")]
    target = int(input())
    print(binarySearch(array, target, 0, array_len-1))

if __name__ == "__main__":
 	main()
