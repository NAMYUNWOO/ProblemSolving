
def quicksortfunc(tlist, first, last):
    if first < last:
        split_point = partition(tlist, first, last)

        quicksortfunc(tlist, first, split_point - 1)
        quicksortfunc(tlist, split_point + 1, last)


def partition(tlist, first, last):
    pivot_value = tlist[first]

    left_mark = first + 1
    right_mark = last

    is_done = False
    while not is_done:
        while left_mark <= right_mark and tlist[left_mark] <= pivot_value:
            left_mark += 1

        while tlist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            is_done = True
        else:
            # Swap
            temp = tlist[left_mark]
            tlist[left_mark] = tlist[right_mark]
            tlist[right_mark] = temp

    temp = tlist[first]
    tlist[first] = tlist[right_mark]
    tlist[right_mark] = temp

    return right_mark


def quick_sort(tlist):
    """
    Run the quick sort
    Do internal sort - tlist will be sorted after finish the task
    :param tlist: target list
    :return: None
    """
    quicksortfunc(tlist, 0, len(tlist) - 1)


def main():
    """
    Entry function of this program
    - Run the quick_sort function
    - Print the before and after list
    :return:
    """
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before: ", alist)
    quick_sort(alist)
    print("After : ", alist)

if __name__ == "__main__":
    main()
