def push(heap, x) :
    heap.append(x)

    index = len(heap)-1

    while index != 1 :
        if heap[index//2] > heap[index] :
            tmp = heap[index//2]
            heap[index//2] = heap[index]
            heap[index] = tmp

            index = index // 2
        else :
            return

def pop(heap) :
    return_value = heap[1]
    heap[1] = heap[-1]

    heap.pop()

    index = 1

    while index < len(heap) :
        minIdx = -1

        if index*2 >= len(heap) :
            break
        elif index*2+1 >= len(heap) :
            minIdx = index*2
        else :
            if heap[index*2] > heap[index*2+1] :
                minIdx = index*2+1
            else :
                minIdx = index*2
    
        if heap[index] <= heap[minIdx] :
            break
        else :
            tmp = heap[index]
            heap[index] = heap[minIdx]
            heap[minIdx] = tmp

            index = minIdx

    return return_value

def heapSort(items) :
    heap = [0]
    result = []

    for i in items :
        push(heap, i)

    for i in range(len(items)) :
        result.append(pop(heap))

    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    print(heapSort(line))

if __name__ == "__main__":
    main()



