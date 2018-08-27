import math

def get_data():
    N = int(input())
    data_list = []
    for _ in range(N):
        num = int(input())
        data_list.append(num)
    return data_list

def sorting_number(numbers):
    s = 0

    # 여기에 문제 1에 대한 코드를 작성하세요.
    while len(numbers) != 1:
        sorted_numbers = sorted(numbers)
        current_s = sum(sorted_numbers[:2])
        s += current_s
        sorted_numbers = sorted_numbers[2:]
        sorted_numbers.append(current_s)
        numbers = sorted_numbers
        
    return s

def main():
    numbers = get_data()

    print (sorting_number_heap(numbers))

if __name__ == '__main__':
    main()
