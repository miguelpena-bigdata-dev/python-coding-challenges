def positiveArray(N, A):
    while True:
        remainder = sum(A) % N
        if remainder == 0:
            return sum(A)
        else:
            A[0] += 1


N = int(input())

temp = input().split()
A = []

for i in range(N):
    A.append(int(temp[i]))

print(positiveArray(N,A))