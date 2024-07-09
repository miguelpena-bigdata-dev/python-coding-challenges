def elementRemoval(N, K, A):
    dict1 = {}
    count_removed = 0
    
    for elem in A:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1
    
    for key in dict1.keys():
        result = dict1[key] % K
        if result != 0:
            count_removed += result
            
    return count_removed

N = int(input())
K = int(input())
temp = input().split()
A = []

for i in range(N):
    A.append(int(temp[i]))

print(elementRemoval(N,K,A))
