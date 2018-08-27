def jjb(schedule):
    '''
        최대로 얻을 수 있는 만족감을 리턴하세요.
    '''
    prev_list = [0] * 3
    cur_list = [0] * 3
    for ele in schedule:
        cur_list[0] = max(prev_list[1], prev_list[2]) + ele[0]
        cur_list[1] = max(prev_list[0], prev_list[2]) + ele[1]
        cur_list[2] = max(prev_list[0], prev_list[1]) + ele[2]
        prev_list = cur_list[:]
    
    return max(prev_list)
    
    
def main():
    '''
        main 함수는 수정하지 마세요!
    '''
    x = int(input())
    y = []
    for i in range(x):
        line = list(map(int, input().strip().split()))
        y.append(line)
    
    print(jjb(y))
if __name__ == "__main__":
    main()
