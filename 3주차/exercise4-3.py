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

    # 이곳에 문제 2에서 작성했던 코드를 붙여넣기 하세요.
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

def move_down(heap):
    parent_idx = 0
    
    # 이곳에 문제 3의 코드를 작성하세요.
    while True:
        child_idx1 = 2 * parent_idx + 1; child_idx2 = 2 * parent_idx + 2
        if child_idx1 > len(heap) - 1:
            break
        elif child_idx1 == len(heap) - 1:
            if heap[parent_idx] > heap[child_idx1]:
                heap[parent_idx], heap[child_idx1] = heap[child_idx1], heap[parent_idx]
            break
        else:
            child_val1 = heap[child_idx1]
            child_val2 = heap[child_idx2]
            if heap[parent_idx] > min([child_val1, child_val2]):
                if child_val1 < child_val2:
                    heap[parent_idx], heap[child_idx1] = heap[child_idx1], heap[parent_idx]
                    parent_idx = child_idx1
                else:
                    heap[parent_idx], heap[child_idx2] = heap[child_idx2], heap[parent_idx]

                    parent_idx = child_idx2
            else:
                break
                
    return heap

def sorting_number_heap(numbers):
    heap = construct_heap(numbers)
    s = 0
    while (len(heap) > 2):
        s1 = heap.pop(0)
        popped = heap.pop()
        heap.insert(0, popped)
        heap = move_down(heap)

        s2 = heap.pop(0)
        popped = heap.pop()
        heap.insert(0, popped)
        heap = move_down(heap)

        ss = s1 + s2

        heap.append(ss)
        heap = move_up(heap)

        s += ss
    s += sum(heap)
    return s

def main():
    numbers = get_data()

    print (sorting_number_heap(numbers))

if __name__ == '__main__':
    main()
