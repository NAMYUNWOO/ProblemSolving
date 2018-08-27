import queue

class Node :
    def __init__(self) :
        self.childs = []

    def addChild(self, x) :
        self.childs.append(x)

def DFS(graph, start, visited) :
    result = [start]
    visited[start] = True

    for v in graph[start].childs :
        if visited[v] == False :
            result = result + DFS(graph, v, visited)

    return result

def BFS(graph, start, visited) :
    myQueue = queue.Queue()

    myQueue.put(start)

    result = [start]
    visited[start] = True

    while myQueue.empty() == False :
        front = myQueue.get()

        for v in graph[front].childs :
            if visited[v] == False :
                myQueue.put(v)

                result = result + [v]
                visited[v] = True

    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[0]

    graph = list(Node() for i in range(n))

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].addChild(line[1])

    for i in range(n) :
        graph[i].childs.sort()

    visited = [False for x in range(n)]
    print(DFS(graph, 0, visited))

    visited = [False for x in range(n)]
    print(BFS(graph, 0, visited ))

if __name__ == "__main__":
    main()



