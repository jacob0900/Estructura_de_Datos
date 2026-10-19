
A =[3,5,2,8,6,4]

def Selection(A):
    for i in range(0,len(A)-2):
        min=i
        for j in range(i+1,len(A)):
            if A[j]<A[min]:
                min=j
        if min != i:
            temp=A[i]
            A[i]=A[min]
            A[min]=temp 
    return A

print(Selection(A))



