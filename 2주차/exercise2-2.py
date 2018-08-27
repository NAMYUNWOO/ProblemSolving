def count_jokbo_length(num_people, scholar, num_relations, relations):
    family_tree = {}
    for i in range(1, num_people+1):
        family_tree[i] = [-1, False]
    for prof, stu in relations:
        family_tree[stu][0] = prof

    a_ancestors = []
    next_up = scholar
    while next_up in family_tree:
        a_ancestors.append(next_up)
        family_tree[next_up][1] = True
        next_up = family_tree[next_up][0]
        
    return len(a_ancestors)

def read_inputs():
    num_people = int(input())
    scholar = int(input())
    num_relations = int(input())
    relations = []
    for i in range(num_relations):
        rel = [int(x) for x in input().split()]
        relations.append((rel[0], rel[1]))

    return num_people, scholar, num_relations, relations

def main():
    num_people, scholar, num_relations, relations = read_inputs()
    ans = count_jokbo_length(num_people, scholar, num_relations, relations)
    print(ans)

if __name__ == "__main__":
    main()