print("Enter number of laptops: ", end="")
N = int(input())
print("Enter starting capital: ", end="")
C = int(input())
print("Enter laptop prices: ", end="")
prices = [0] + [int(x) for x in input().split()]
print("Enter laptop gains: ", end="")
gains = [0] + [int(x) for x in input().split()]
table = [[0] * (C + 1) for _ in range (N + 1)]

for i in range(1, N + 1):
    for j in range(0, C + 1):
        table[i][j] = table[i-1][j]
        if prices[i] <= j:
            table[i][j] = max(table[i][j], table[i-1][j-prices[i]] + gains[i])

print("Capital at the end of the summer:", C + max(table[N]))
