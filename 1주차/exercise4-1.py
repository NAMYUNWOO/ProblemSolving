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

def read_input():
    data = input().strip()
    return (data)

def main():
    given_input = read_input()

    if given_input == 'w' or given_input == 'b':
        print (given_input)
    else:    
        tree = input2tree(given_input)
        print (tree)        

if __name__ == '__main__':
    main()