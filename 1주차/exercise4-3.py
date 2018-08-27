def input2tree(given_input):
    buffer = [ch for ch in given_input]

    def _build(tree, buffer):
        while buffer:
            alphabet = buffer.pop(0)
            if alphabet == 'x':
                tree.append(_build([], buffer))
            else:
                tree.append(alphabet)

            if len(tree) == 4:
                break

        return tree

    return_tree = _build([], buffer)

    return return_tree

def tree2output(tree, output_str):
    if len(tree) == 1:
        tree = tree[0]
    for i in range(4):
        if isinstance(tree[i], str) == False:
            output_str += 'x'
            output_str = tree2output(tree[i], output_str)
        else:
            output_str += tree[i]
    return output_str

def flip_tree(tree):
    return_tree = [None]*4
    for i in range(4):
        if isinstance(tree[i], str) == False:
            return_tree[(i+2)%4] = flip_tree(tree[i])
        else:
            return_tree[(i+2)%4] = tree[i]

    return return_tree

def read_input():
    data = input().strip()
    return (data)

def main():
    given_input = read_input()

    if given_input == 'w' or given_input == 'b':
        print (given_input)
    else:    
        tree = input2tree(given_input)
        initial_str = 'x'
        answer_output = tree2output(tree, initial_str)
        print (answer_output)        

if __name__ == '__main__':
    main()