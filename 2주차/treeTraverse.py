class Node :
    def __init__(self) :
        self.left = -1
        self.right = -1

    def setChilds(self, l, r) :
        self.left = l
        self.right = r

def postorder(binaryTree, r) :
    result = []

    leftChild = binaryTree[r].left
    rightChild = binaryTree[r].right

    if leftChild != -1 :
        result = postorder(binaryTree, leftChild)

    if rightChild != -1 :
        result = result + postorder(binaryTree, rightChild)

    result = result + [r]

    return result

def main():
    '''
    Do not change this code
    '''

    n = int(input())

    binaryTree = list(Node() for i in range(n))

    for i in range(n) :
        line = [int(x) for x in input().split()]

        binaryTree[line[0]].setChilds(line[1], line[2])

    print(postorder(binaryTree, 0))

if __name__ == "__main__":
    main()



