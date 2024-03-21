

# 1. Characterize the structure of an optimal solution
# 2. Recursively define the value of an optimal solution
# 3. Compute the value of an optimal solution
# 4. Construct an optimal solution from computed information

# Goal is to determine an order for multiplying matrices that has the lowest cost
import sys
def matrix_chain_order(p):
    
    n = len(p)
    m = [[0 for x in range(n)] for y in range(n)]
    s = [[0 for x in range(n)] for y in range(n)]

    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m[1][n - 1]






# Example
array1 = [10, 100, 5, 50]
array2 = [30, 35, 15, 5, 10, 20, 25]
print("Minimum number of multiplications of array1 is", str(matrix_chain_order(array1)))
print("Minimum number of multiplications of array2 is", str(matrix_chain_order(array2)))

