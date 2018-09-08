import timeit, time

def sequentialfn():
    dList = [1,2,3,4,5,3]
    dItem = 21
    pos = 0
    while pos < len(dList) and True:
        if dItem == dList[pos]:
            return True
        else:
            pos += 1
    return False


print(sequentialfn())
thetime = timeit.Timer('sequentialfn()', 'from __main__ import sequentialfn')
print('Sequential Search Time: ', thetime.timeit(), 'milliseconds')

def binaryfn(randomlist, dItem):
    if len(randomlist) <= 1:
        return False
    else:
        middleList = len(randomlist) // 2
        if dItem == randomlist[middleList]:
            return True
        else:
            if dItem < randomlist[middleList]:
                return binaryfn(randomlist[:middleList], dItem)
            else:
                return binaryfn(randomlist[middleList + 1:], dItem)


random_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binaryfn(random_list, 3))

#thetime2 = timeit.Timer('binaryfn(random_list , dItem)', 'from __main__ import binaryfn')
#print('Binary Search Time: ', thetime2.timeit(), 'milliseconds')
