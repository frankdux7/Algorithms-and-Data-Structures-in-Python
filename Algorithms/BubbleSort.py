L = [4,6,5,1,3,2,7,11,9,10,8]

def bubbleSort(L):
    for i in range(len(L)):
        j = i + 1
        for j in range(i, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    return L

print(bubbleSort(L))
