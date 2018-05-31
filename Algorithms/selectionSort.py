

def selectionSort(L):
    for i in range(len(L)):
        j = i+1
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

L = [4,6,5,1,3,2,7,11,9,10,8]
print(selectionSort(L))
