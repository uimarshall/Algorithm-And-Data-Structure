def mergeSort(ls):
    if len(ls)>1:
        mid = len(ls)//2
#split the list into two
        lefthalf = ls[:mid]
        righthalf = ls[mid:]
# call the mergeSort function each half
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0 #initialising the sorted list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                ls[k]=lefthalf[i]
                i=i+1
            else:
                ls[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            ls[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            ls[k]=righthalf[j]
            j=j+1
            k=k+1

    smallest_number = ls[0]

    return smallest_number

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
print(mergeSort(alist))
