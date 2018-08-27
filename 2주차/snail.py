def isRightPosition(arr, y, x) :
    height = len(arr)
    width = len(arr[0])

    if y >= 0 and y < height and x >= 0 and x < width and arr[y][x] == 0 :
        return True
    else :
        return False

def getSnail(n) :
    result = []

    for i in range(n) :
        result.append([0] * n)

    ky = [0, 1, 0, -1]
    kx = [1, 0, -1, 0]

    pos = 0
    number = 1
    y = 0
    x = 0

    for c in range(1, n*n+1, 1) :
        result[y][x] = c

        if c == n*n :
            break

        while True :
            if isRightPosition(result, y + ky[pos], x + kx[pos]) :
                y = y + ky[pos]
                x = x + kx[pos]

                break
            else :
                pos = (pos + 1) % 4

    return result

def main():
    '''
    Do not change this code
    '''

    n = int(input())

    snail = getSnail(n)

    for i in range(n) :
        line = ""
        for j in range(n) :
            line = line + str(snail[i][j])
            line = line + " " 
        print(line)

if __name__ == "__main__":
    main()



