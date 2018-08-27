import elice_utils

def take_my_money(amount_to_return, units):
    #여기에 함수를 구현해 주세요.
    changes = list()
    for unit in units:
        changes.append(amount_to_return//unit)
        amount_to_return = amount_to_return % unit
    return changes 

def main():
    K = int(input())
    for k in range(K):
        # 여기에 입력받는 부분을 구현해 주세요.
        input()
        units = map(int, input().split())
        amount_to_return = int(input())

        # 함수 호출과 출력을 위한 부분입니다. 수정하지 마세요.
        print(" ".join(map(str,take_my_money(amount_to_return, units))))
    
if __name__ == "__main__":
    main()
