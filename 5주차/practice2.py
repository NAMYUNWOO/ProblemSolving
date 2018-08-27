def get_wine_list(lst):
    def max_ind(lst):
        res = 0
        for idx, elem in enumerate(lst):
            if elem > lst[res]:
                res = idx
        return res
    
    def get_part_sum(lst, idx_lst):
        return sum([elem for idx, elem in enumerate(lst) if idx in idx_lst])
    
    if len(lst) <= 2:
        return [idx+1 for idx in range(len(lst))]
    elif len(lst) == 3:
        case = max_ind([lst[0]+lst[1], lst[0]+lst[2], lst[1]+lst[2]])
        if case == 0:
            return [1,2]
        elif case == 1:
            return [1,3]
        else:
            return [2,3]
    else:
        res = [[1], [1,2], get_wine_list(lst[:3])]
        for i in range(3, len(lst)):
            case = max_ind([get_part_sum(lst, res[i-3])+lst[i-1]+lst[i], 
                            get_part_sum(lst, res[i-2])+lst[i], 
                            get_part_sum(lst, res[i-1])])
            if case == 0:
                res.append(res[i-3]+[i, i+1])
            elif case == 1:
                res.append(res[i-2]+[i+1])
            else:
                res.append(res[i-1])
        return res[-1]
    
def main():
    n = int(input())
    tmp = []
    for i in range(n):
        tmp.append(int(input()))
        
    res = get_wine_list(tmp)
    for elem in res:
        print(elem)
    
    
if __name__ == '__main__':
    main()