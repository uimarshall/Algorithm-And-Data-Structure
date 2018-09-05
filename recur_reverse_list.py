
def reverse(lst):
    '''the base condition is that if the length of the list is equal to 0, the list is returned.'''
    if len(lst) == 0:
        return lst
    else:
        '''recursive case: If not equal to 0, the reverse function is recursively called to slice
        the part of the list except the first character and concatenate
        the first character to the end of the sliced list.'''
        return reverse(lst[1:]) + [lst[0]]
# Demo: will output  ['a', 'b', 'c', 'd', 'e']
a = ['e','d','c','b','a']
print(reverse(a))
