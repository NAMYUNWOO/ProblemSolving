def mergeSort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        lefthalf = input_list[:mid]
        righthalf = input_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                input_list[k] = lefthalf[i]
                i += 1
            else:
                input_list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            input_list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            input_list[k] = righthalf[j]
            j += 1
            k += 1