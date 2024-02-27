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

def knapsack_fractional(n, W):
    kg, price = random_knapsack_problem(n, W)
    price_to_weight_ratio = [(price[i] / kg[i], i) for i in range(n)]
    price_to_weight_ratio.sort(reverse=True) 

    sum_value = 0
    current_weight = 0

    print("Selected items:")
    for i in range(n):
        if current_weight + kg[price_to_weight_ratio[i][1]] <= W:
            current_weight += kg[price_to_weight_ratio[i][1]]
            sum_value += price[price_to_weight_ratio[i][1]]
            print("Item:", price_to_weight_ratio[i][1] + 1, "Weight:", kg[price_to_weight_ratio[i][1]], "Value:", price[price_to_weight_ratio[i][1]])
        else:
            available_weight = W - current_weight
            print("Available weight:", available_weight)
            remaining_value = available_weight * price_to_weight_ratio[i][0]
            sum_value += remaining_value
            print("Item:", price_to_weight_ratio[i][1] + 1, "has Weight:", kg[price_to_weight_ratio[i][1]], "and Value:", price[price_to_weight_ratio[i][1]], "But we are taking only this much of its value:", remaining_value)
            break
    
    return sum_value


def random_knapsack_problem(n, W):
    kg = [random.randint(1, 10) for _ in range(n)]
    price = [random.randint(1, 100) for _ in range(n)]

    return kg, price

n = 5
W = 10
print("Maximum value:", knapsack_fractional(n, W))