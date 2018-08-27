class Node :
    def __init__(self) :
        self.left = -1
        self.right = -1

    def setChilds(self, l, r) :
        self.left = l
        self.right = r


def preorder(tree, r):
	result = ""

	#implement here...
	if r == -1:
		return ""
	curNode = r
	leftNode = preorder(tree, tree[r].left)
	rightNode = preorder(tree, tree[r].right)
	result += str(curNode) + str(leftNode) + str(rightNode)

	return result


def postorder(tree, r):
	result = ""

	#implement here...
	if r == -1 :
		return ""
	leftNode = postorder(tree, tree[r].left)
	rightNode = postorder(tree, tree[r].right)
	curNode = r
	result += str(leftNode) + str(rightNode) + str(curNode)

	return result


def inorder(tree, r):
	result = ""

	#implement here...
	if r == -1:
		return ""
	leftNode = inorder(tree, tree[r].left)
	curNode = r
	rightNode = inorder(tree, tree[r].right)
	result += str(leftNode) + str(curNode) + str(rightNode)

	return result



def main():
    '''
    Do not change this code.
    '''

    n = int(input())

    binaryTree = list(Node() for i in range(n+1))

    for i in range(n) :
        line = [int(x) for x in input().strip().split()]
        binaryTree[line[0]].setChilds(line[1], line[2])

    print('preorder traversal result:')
    print(preorder(binaryTree, 1))
    print('postorder traversal result:')
    print(postorder(binaryTree, 1))
    print('inorder traversal result:')
    print(inorder(binaryTree, 1))

if __name__ == "__main__":
 	main()



