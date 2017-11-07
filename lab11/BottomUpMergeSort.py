def merge(A1, A2):
    e1 = len(A1)
    e2 = len(A2)
    c1 = c2 = 0
    l = []
    while c1 < e1 or c2 < e2:
        if c1 < e1 and c2 < e2 and A1[c1] <= A2[c2]:
            l.append(A1[c1])
            c1 += 1
        elif c1 < e1 and c2 < e2:
            l.append(A2[c2])
            c2 += 1
        elif c1 < e1:
            l.append(A1[c1])
            c1 += 1
        else:
            l.append(A2[c2])
            c2 += 1
    return l


def mergeSort(A):
    i = 1
    while i < len(A):
        j = 0
        while j < len(A):
            A[j: 2*i+j+1] = merge(A[j: i+j], A[i+j: 2*i+j+1])
            j += 2*i
        i = 2*i
    return A


print(mergeSort([4, 1, 8, 12, 6, 2, 9, 5]))
