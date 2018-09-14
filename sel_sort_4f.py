import statistics

def bubble_sort(some_list):
    is_sorted = False
    last_sorted_item = len(some_list)-1
    while not is_sorted:
        is_sorted = True
        for i in range(0, last_sorted_item):
            if some_list[i] > some_list[i+1]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
                is_sorted = False
        last_sorted_item -= 1

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]

#=============================================================================

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def get_pivot_value(a_list, first, last):
    value_list = []
    value_list.append(a_list[first])
    value_list.append(a_list[last])
    value_list.append(a_list[len(a_list) // 2])
    pivot_value = statistics.median(value_list)
    return pivot_value

def partition(a_list, first, last):
    #pivot_value = a_list[first]
    pivot_value = get_pivot_value(a_list, first, last)
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#bubble_sort(a_list)
#selection_sort(a_list)
quick_sort(a_list)
print(a_list)

'''
The complexity for the "median-of-three method for selecting a pivot value"
is 0.049182891845703125 while the complexity for "the technique where the first
item is used as a pivot" is 0.002001523971557617. Thus, median of three method
is slower compared to the other technique.
'''
