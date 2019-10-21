# sorting a list in 3 ways.
import random  # needed to generate random array
import datetime
import sys

sys.setrecursionlimit(1000001)


def quick_sort(array, lo, hi):
    if lo < hi:  # will end when low == hi
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)


def partition(a, lo, hi):
    pivot = a[hi - 1]
    i = lo
    for j in range(lo, hi - 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi - 1] = a[hi - 1], a[i]
    return i


def bubble_sort(a, hi):
    found = True
    while found:
        found = False
        for i in range(0, hi - 1):
            if a[i] > a[i + 1]:
                found = True
                a[i], a[i + 1] = a[i + 1], a[i]


def merge_sort(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    # print("Merging ", alist)


hi = int(input("How many elements to sort?"))
a = []
for i in range(0, hi):
    a.append(random.randint(1, 10000))
b = a.copy()
c = a.copy()
print("Initial list:", a)

start = datetime.datetime.now()
quick_sort(a, 0, hi)
print("quick_Sort time was: ", datetime.datetime.now() - start)
start = datetime.datetime.now()
bubble_sort(b, hi)
print("bubble_sort time was: ", datetime.datetime.now() - start)

start = datetime.datetime.now()
merge_sort(c)
print("merge_sort time was: ", datetime.datetime.now() - start)
print("Sorted list:", a)

# Which sort is the best? Which is the worst?
# Which of the algorithms are recursive?
"""
The best algorithm is the Quick Sort. This is because it avoids comparing all of the values to each other. The Merge
Sort follows a similar principal. Still takes twice the time. On the other hand the Bubble Sort is the worst by far.
It compares each value, as they move upwards (like a bubble). This increases considerably the number of iterations.

Both the Quick Sort and the Merge Sort are recursive. This means that they "call" themselfs during exection. This can 
be seen in lines 12 & 13 for the Quick Sort, and on lines 44 & 45 on the Merge Sort.
"""