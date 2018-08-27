def sum_0(data):
    return_value = 1e300
    return_pair = [None, None]

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            sum_i_j = abs(data[i] + data[j])
            if sum_i_j < return_value:
                return_value = sum_i_j
                return_pair = sorted([data[i], data[j]])

    return(return_pair)

def read_input():
    given_data = input()
    data = [int(v.strip()) for v in given_data.split()]
    
    return (data)

def main():
    data = read_input()
    print (sum_0(data))

if __name__ == "__main__":
    main()