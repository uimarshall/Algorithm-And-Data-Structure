'''Perform a benchmark analysis for a shell sort, using different increment sets
on the same list.

In Python, we can benchmark a function by noting the starting time and ending time with respect to the system we are using.'''

import timeit, time
def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        end = time.time()
        print('\nThe Benchmark  for increment of size', sublist_count, 'is ', end - start)

        print("After increments of size", sublist_count, "The list is",a_list)
        sublist_count = sublist_count // 2


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]



def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


shell_sort(a_list)
print('\nThe sorted list is',a_list)
