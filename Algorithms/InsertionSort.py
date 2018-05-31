L = [4,6,5,1,3,2,7,11,9,10,8]

def insertionSort(L):
    '''
    Сравава текущата стойност и я премества наляво, докато тази в ляво не е по малка от текущата.
    Проверява докато индексът на предишната стойност не стане по-малък от нула
    '''
    for i in range(1, len(L)):
        curr = i
        prev = i - 1
        while prev >= 0:
            if (L[curr] < L[prev]):
                L[curr], L[prev] = L[prev], L[curr]
                curr -= 1
                prev -= 1

            else:
                break

    return L

print(insertionSort(L))




