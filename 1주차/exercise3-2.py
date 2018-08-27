def sum_0(data):
    data = sorted(data)

    if data[0] > 0:
        return_pair = [data[0], data[1]]
        return_value = abs(sum(return_pair))
    elif data[-1] < 0:
        return_pair = [data[-2], data[-1]]
        return_value = abs(sum(return_pair))
    else:
        return_value = 1e300
        return_pair = [None, None]
        st_idx = 0
        end_idx = len(data) - 1
        while st_idx < end_idx:
            if return_value > abs(data[st_idx] + data[end_idx]):
                return_value = abs(data[st_idx] + data[end_idx])
                return_pair[0] = data[st_idx]
                return_pair[1] = data[end_idx]
            if data[st_idx] + data[end_idx] > 0:
                end_idx -= 1
            else: 
                st_idx += 1
    
    return return_pair

def read_input():
    given_data = input()
    data = [int(v.strip()) for v in given_data.split()]
    
    return (data)

def main():
    data = read_input()
    print (sum_0(data)) # sum_0 함수를 써서 예시에 대한 답을 확인 해 보세요.

if __name__ == "__main__":
    main()