'''Implement the bubble sort using simultaneous assignment.

In Python, it is possible to perform simultaneous assignment. The statement a, b = b, a
will result in two assignment statements being done at the same time (see Figure 5.14). Using
simultaneous assignment, the exchange operation can be done in one statement.'''

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp, a_list[i] = a_list[i], a_list[i + 1]
                a_list[i + 1] = temp


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)
