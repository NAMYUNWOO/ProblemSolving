def jjb2(schedule):
    def getValids(idx, slist):
        return_list = [v for i, v in enumerate(slist) if i != idx]
        return return_list
    
    curResult = schedule[0]
    path = [["jja"],["jjam"],["bbok"]]
    
    for curSchedule in schedule[1:]:
        temResult = []
        tempPath = path[:]

        for j in range(3):
            bigger = max(getValids(j, curResult))

            biggerIndexList = [k for k, v in enumerate(curResult) if v == bigger and k != j]
            biggerIndex = biggerIndexList[0]
            
            path[j] = (tempPath[biggerIndex] + [index2menu(j)])
            temResult.append(curSchedule[j] + bigger)
        curResult = temResult

    maxResult = max(curResult)
    maxIndex = curResult.index(maxResult)

    return path[maxIndex]

def index2menu(idx):
    """
        index 0,1,2를 짜, 짬, 볶으로 변환해주는 함수
        쓰셔도 되고, 안 쓰셔도 됩니다~
    """
    if idx == 0:
        return "jja"
    elif idx == 1:
        return "jjam"
    elif idx == 2:
        return "bbok"

def main():
    x = int(input())
    y = []
    for i in range(x):
        line = list(map(int, input().strip().split()))
        y.append(line)

    print(jjb2(y))
if __name__ == "__main__":
    main()
