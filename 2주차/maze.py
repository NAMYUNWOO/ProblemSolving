import queue

def isOkay(y, x, n, m, weight, maze) :
    if y >= 0 and y < n and x >= 0 and x < m and maze[y][x] == 0 and weight[y][x] == 0 :
        return True
    else :
        return False

def findSolution(n, m, maze) :
    ky = [-1, 0, 0, 1]
    kx = [0, 1, -1, 0]

    weight = [[0 for x in range(m)] for x in range(n)]

    weight[n-1][0] = 1
    myQueue = queue.Queue()

    myQueue.put((n-1, 0))

    while myQueue.empty() == False :
        current = myQueue.get()

        y = current[0]
        x = current[1]

        for i in range(4) :
            yy = y + ky[i]
            xx = x + kx[i]

            if isOkay(yy, xx, n, m, weight, maze) :
                weight[yy][xx] = weight[y][x] + 1
                myQueue.put((yy, xx))

    return weight[0][m-1]-1

def main():
    '''
    Do not change this code
    '''

    firstLine = [int(x) for x in input().split()]

    n = firstLine[0]
    m = firstLine[1]

    myMap = []

    for i in range(n) :
        firstLine = [int(x) for x in input().split()]

        myMap.append(firstLine)

    print(findSolution(n, m, myMap))

if __name__ == "__main__":
    main()



