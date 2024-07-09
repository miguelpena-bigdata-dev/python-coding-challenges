import math
def positiveArray(N, A):
    return N * math.ceil(sum(A)/N)


N = int(input())

temp = input().split()
A = []

for i in range(N):
    A.append(int(temp[i]))

print(positiveArray(N,A))
