a = [3, 7, 5, 1, 4, 10, 12, 1, 23, 3]
def bubble_sort(array):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[0]
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

print(QuickSort(a))





