
def bubble_sort(tlist):
    """
    Run the bubble sort
    Do internal sort - tlist will be sorted after finish the task
    :param tlist: target list
    :return: None
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(tlist)-1):
            if tlist[i] > tlist[i+1]:
                temp = tlist[i]
                tlist[i] = tlist[i+1]
                tlist[i+1] = temp
                changed = True


def main():
    """
    Entry function of this program
    - Run the buuble_sort function
    - Print the before and after list
    :return:
    """
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before: ", alist)
    bubble_sort(alist)
    print("After : ", alist)

if __name__ == "__main__":
    main()
