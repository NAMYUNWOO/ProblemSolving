def get_parent_child_rel():
    p_c_rel = dict()
    all_childs = set()
    no_rels = int(input())
    for _ in range(no_rels):
        tmp = [int(v) for v in input().split()]
        p_c_rel[tmp[0]] = {'left' :  tmp[1], 'right' : tmp[2]}
        for child in tmp[1:]:
            if child != -1:
                all_childs.add(child)
    root_node = list(set(range(1, no_rels + 1)) - all_childs )[0]
    return p_c_rel, root_node

def inorder_traverse(rel, target_node, order_list, node_level):
    if target_node == -1: return
    current_rel = rel[target_node]
    current_level = node_level[target_node]

    if current_rel['left'] != -1: node_level[current_rel['left']] = current_level + 1
    if current_rel['right'] != -1: node_level[current_rel['right']] = current_level + 1

    # 이곳에 문제 1에 대한 코드를 작성하세요.
    inorder_traverse(rel, current_rel['left'], order_list, node_level)
    order_list.append(target_node)
    inorder_traverse(rel, current_rel['right'], order_list, node_level)
    
    return [order_list, node_level]

def main():
    rel, root_node = get_parent_child_rel()

    order_list, node_level = inorder_traverse(rel, root_node, [], {root_node : 1})
    level_node = dict()
    for k, v in node_level.items():
        if v in level_node:
            level_node[v].append(k)
        else:
            level_node[v] = [k]
    print (get_max_width(order_list, level_node))

if __name__ == '__main__':
    main()