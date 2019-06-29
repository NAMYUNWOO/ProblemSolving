import sys
sys.setrecursionlimit(15000)
cache = [ [[-1 for _ in range(101)] for _ in range(101)] for _ in  range(2)]
endidx = 0
def sfunction(idx,cur,rest):
    global endidx,cache
    if (idx ==  endidx) and (rest >0):
        return 0
    if endidx - idx < rest:
        return 0
    if (idx == endidx) and (rest == 0):
        return  1
    iidx = endidx - idx 
    if cache[cur][iidx][rest] != -1:
        return cache[cur][iidx][rest]
    if (cur == 0):
        cache[cur][iidx][rest] = sfunction(idx + 1 , 1 , rest) + sfunction(idx+1,0,rest)
    else:
        if rest  == 0:
            cache[cur][iidx][rest] = sfunction(idx + 1 , 0 , rest)
        else:
            cache[cur][iidx][rest] = sfunction(idx + 1 , 1 , rest-1) + sfunction(idx+1,0,rest)
    return cache[cur][iidx][rest]
def main():
    global endidx, cache 
    tc = int(input())
    for _ in range(tc):
        inputi = input()
        _endidx,k=list(map(lambda x : int(x) ,inputi.strip().split(" ")))
        endidx = _endidx - 1
        ans=sfunction(0,0,k)+sfunction(0,1,k)
        #cache = [ [[-1 for _ in range(101)] for _ in range(101)] for _ in  range(2)]
        print(ans)
if __name__ == "__main__":
    main()