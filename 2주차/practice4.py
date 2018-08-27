import elice_utils

def sort_by_first_element(lst):
    '''
    순서쌍의 list를 입력받아서 정렬하는 함수입니다. 
    순서쌍의 첫번째 원소를 기준으로 정렬하는 함수를 작성하세요. 
    
    ex) sort_by_first_element([(1,1), (3,4), (2,5)]) returns [(1,1), (2,5), (3,4)]
    '''
    return sorted(lst, key=lambda x: x[0])
    
def main():
    n = input()
    a = []
    for i in range(n):
        tmp = input().strip().split()
        a.append(tmp)
    
    
    print(sort_by_first_element(a))
    

if __name__ == "__main__":
    main()
