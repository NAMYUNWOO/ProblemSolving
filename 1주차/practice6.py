def binary_search(lst, cond):
    '''
    Function to implement.
    Use idea of binary search to find minimum element that satisfies the cond predicate. 
    You can assume that cond function is always true for numbers that are larger than the threshold, and always false otherwise. 
    You can assume that lst is a sorted list of integers. (In increasing order)
    
    ex) binary_search([1,2,3,4,5], lambda x: x>1) returns 2
    '''
    res = -1
    l = 0
    r = len(lst)-1
    m = int((l+r)/2)
    
    while l != m:
        if cond(lst[m]):
            r = m 
            m = int((l+r)/2)
        else: 
            l = m 
            m = int((l+r)/2)
        
    if cond(lst[m]):
        print(lst[m])
        return lst[m]
    else:
        print(lst[m+1])
        return lst[m+1]
    
    
    
def find_min_square_root(n):
    '''
    Function to implement
    Find minimum q such that satisfies q^2 > n. 
    Use above binary search you have implemented. 
    '''
    return binary_search(range(int(n/2)), lambda x:x*x>=n)
    
    
def main():
    '''
    Do not change this code
    '''
    testcase = int(input())
    return find_min_square_root(testcase)
    
if __name__ == '__main__':
    main()
    