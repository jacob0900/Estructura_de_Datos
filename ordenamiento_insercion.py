A = [3, 5, 2, 8, 6, 4]

def Insercion(A):
    for i in range(1, len(A)):
        j = i
        while(j > 0 and A[j-1] > A[j]):
            temp = A[j]
            A[j] = A[j-1] 
            A[j-1] = temp
            j -= 1
           
    return A

print(Insercion(A))

