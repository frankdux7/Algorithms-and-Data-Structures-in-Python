

def selection_sort(L):

    for i in range(len(L)):
        min_position = i
        for j in range(i+1, len(L)):
            if L[min_position] > L[j]:
                min_position = j

        L[min_position], L[i] = L[i], L[min_position]

    return L

L = [4,6,5,1,3,2,7,11,9,10,8]
print(selection_sort(L))
