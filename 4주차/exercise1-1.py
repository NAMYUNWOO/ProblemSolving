def find_max_sum(num_size, matrix):
    # 구현해주세요!
    # 주의: 현재 matrix에는 피라미드가 역으로 들어가 있습니다.
    # 예) [[4, 5, 2, 6, 5], [2, 7, 4, 4], [8, 1, 0], [3, 8], [7]]
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i-1][j] > matrix[i-1][j+1]:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += matrix[i-1][j+1]

    return matrix[num_size-1][0]

def read_inputs():
    num_size = int(input())
    matrix = []
    for i in range(num_size):
        line = [int(x) for x in input().split()]
        # 피라미드를 역으로 뒤집어 입력 받습니다:
        # 피라미드의 꼭대기에서부터 답을 구하며 내려오면 최종 답이
        # 맨 아래에 위치하게 되는데, 그러면 최대값을 찾는데 
        # O(num_size)만큼의 시간이 소요됩니다. 반면 아래에서 위로
        # 올가면서 답을 구하면 최대값은 피라미드 정상에 위치하므로
        # 답을 바로 출력할 수 있습니다.
        matrix.insert(0, line)
        # matrix.append(line)은 line이 matrix의 뒤에 붙는 경우이며
        # matrix.insert(0, line)은 0번째에 line을 삽입합니다.

    return num_size, matrix

def main():
    num_size, matrix = read_inputs()
    ans = find_max_sum(num_size, matrix)
    print(ans)

if __name__ == "__main__":
    main()