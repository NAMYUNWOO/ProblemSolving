def get_max_wine(lst):
    if len(lst) <= 2:
        return sum(lst)
    elif len(lst) == 3:
        return max(lst[1]+lst[2], lst[0]+lst[1], lst[0]+lst[2])
    else:
        res = [lst[0], 
                lst[0]+lst[1],
                max(lst[1]+lst[2], lst[0]+lst[1], lst[0]+lst[2])]
        for i in range(3, len(lst)):
            res.append(max(res[i-3]+lst[i-1]+lst[i],
                        res[i-2]+lst[i],
                        res[i-1]))
        return res[-1]
    
def main():
    n = int(input())
    tmp = []
    for i in range(n):
        tmp.append(int(input()))
        
    print(get_max_wine(tmp))
    
if __name__ == '__main__':
    main()