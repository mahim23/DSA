from lab7.BinaryHeap import BinaryHeap


def heapSort(l):
    H = BinaryHeap(l)
    for i in range(H.len):
        elem = H.extractMax()
        H.heap.append(elem)

    return H.heap


def main():
    l = input("Enter list to be sorted: ")
    l = list(map(int, l.split()))
    print(heapSort(l))


if __name__ == '__main__':
    main()
