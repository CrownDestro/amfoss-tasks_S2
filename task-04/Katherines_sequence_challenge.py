t=int(input())
while t>0:
    n= int(input())
    sequence = []
    for i in range(1,n):
        for j in range(1,n-1):
            l = list(map(int, input().split()))
            sequence.append(l)
    t = t-1
    original_permutation = []
    for k in range(n):
        for num in range(1, n + 1):
            if num not in sequences[i]:
                original_permutation.append(num)
                break
print(original_permutation)