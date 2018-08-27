import elice_utils

class Node :
    def __init__(self) :
        self.children = []
        self.color = 0 # 0 for no color, 1 for red, 2 for green

    def addChild(self, x) :
        self.children.append(x)

def bicolor(graph):
    #여기에 함수를 구현해 주세요
    #graph가 bicolorable이라면 True를, 아니라면 False를 리턴해 주세요
    st = [] # stack
    n_uncolored = len(graph)
    while n_uncolored > 0: # 비 연결 그래프의 경우를 위해 while문 이용
        uncolored_nodes = [node for node in graph if node.color is 0]
        if len(uncolored_nodes) is 0:
            return False
        st.append(uncolored_nodes[0]) # 색칠이 안 된 첫 꼭짓점을 스택에 추가
        n_uncolored -= 1
        uncolored_nodes[0].color = 1 # 첫 꼭짓점을 임의의 색으로 색칠
        while len(st)>0:
            v = st.pop()
            for child_index in v.children:
                child = graph[child_index]
                if child.color is v.color:
                    return False
                elif child.color is 0:
                    child.color = 3-v.color
                    st.append(child)
                    n_uncolored -= 1
    return True

def main():
    K = int(input())
    for k in range(K):
        # 여기에 입력받는 부분을 구현해 주세요
        N, M = map(int,input().split())
        graph = [Node() for i in range(N)]
        for m in range(M):
            a, b = map(int,input().split())
            graph[a].addChild(b)
            graph[b].addChild(a)
        if bicolor(graph):
            print('T')
        else:
            print('F')
    
if __name__ == "__main__":
    main()
