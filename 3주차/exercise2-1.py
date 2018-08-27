def find_min_room(num_class, classes):
    classes_start = sorted([x[1] for x in classes])
    classes_end = sorted([x[2] for x in classes])

    match = 0
    for i, start in enumerate(classes_start):
        if start >= classes_end[match]:
            match += 1

    return len(classes) - match

def read_inputs():
    num_class = int(input())
    classes = []
    for i in range(num_class):
        line = [int(x) for x in input().split()]
        class_no = line[0]
        start = line[1]
        end = line[2]
        classes.append((class_no, start, end))

    return num_class, classes

def main():
    num_class, classes = read_inputs()
    ans = find_min_room(num_class, classes)
    print(ans)

if __name__ == "__main__":
    main()