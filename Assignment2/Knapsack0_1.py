import random
# The 0-1 knapsack problem

# A thief robbing a store find n items
# the i-th item is worth v[i] dollars and weighs w[i] pounds, where v[i] and w[i] are integers
# thief wants to take as valuable a load as possible, but he can carry at most W pounds in his knapsack for some integer W
# which items should he take?

# The fractional knapsack problem

# The setup is the same, but the thief can take fractions of items rather than (0-1).
# Think of an items in the 0-1 knapsack problem as being like a gold ingot,
# and an items in the fractional knapsack problems as more like gold dust. 


# Have to look at all items and possible weights smaller than W
# Have to build a table where n+1 is the number of items and W+1 is the weight
def knapsack_0_1(n, W):
    kg, price = random_knapsack_0_1(n, W)
    K = [[0 for j in range(W + 1)] for i in range(n + 1)] # Initializing the n+1 x W+1 table

    for i in range(1, n + 1): # i is the number of items
        for j in range(1, W + 1): # j is the weight
            if j < kg[i - 1]:
                K[i][j] = K[i - 1][j] 
            else: 
                K[i][j] = max(K[i - 1][j], K[i - 1][j - kg[i - 1]] + price[i - 1]) 
    
    print("Selected items:")
    i, j = n, W
    while i > 0 and j > 0:
        if K[i][j] != K[i - 1][j]:  
            print("Item:", i, "Weight:", kg[i - 1], "Value:", price[i - 1])
            j -= kg[i - 1] 
        i -= 1 

    return K[n][W] 

def random_knapsack_0_1(n, W):
    # Random vlaues for n and W
    kg = [random.randint(1, 10) for _ in range(n)]
    price = [random.randint(1, 100) for _ in range(n)]
    return kg, price

n = 10
W = 10

print("Maximum value:", knapsack_0_1(n, W))
    