import math

def get_data():
    N = int(input())
    data_list = []
    for _ in range(N):
        num = int(input())
        data_list.append(num)
    return data_list

def construct_heap(numbers):
    heap = []
    while len(numbers) != 0:
        number_ = numbers.pop()
        heap.append(number_)
        heap = move_up(heap)
    return heap

def move_up(heap):
    child_idx = len(heap) - 1

    # 아래에 문제 2에 대한 코드를 작성하세요.
    while True:
        parent_idx = int(math.floor((child_idx - 1) / 2))
        if heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
            child_idx = parent_idx
            if child_idx == 0:
                break
        else:
            break
            
    return heap

def main():
    numbers = get_data()
    heap = construct_heap(numbers)

    print (heap)

if __name__ == '__main__':
    main()
