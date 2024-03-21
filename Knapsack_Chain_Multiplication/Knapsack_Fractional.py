import random

def knapsack_fractional(n, W):
    kg, price = random_knapsack_problem(n, W)
    price_to_weight_ratio = [(price[i] / kg[i], i) for i in range(n)]
    price_to_weight_ratio.sort(reverse=True)

    total_value = 0
    current_weight = 0

    print("Selected items:")
    for _, i in price_to_weight_ratio:
        if current_weight + kg[i] <= W:
            current_weight += kg[i]
            total_value += price[i]
            print("Item:", i + 1, "Weight:", kg[i], "Value:", price[i])
        else:
            remaining_capacity = W - current_weight
            fractional_value = remaining_capacity * (price[i] / kg[i])
            total_value += fractional_value
            print("Item:", i + 1, "has Weight:", kg[i], "and Value:", price[i], "but due to weight capacity we only take:", fractional_value)
            break

    return total_value

def random_knapsack_problem(n, W):
    kg = [random.randint(1, 10) for _ in range(n)]
    price = [random.randint(1, 100) for _ in range(n)]
    return kg, price

n = 5
W = 10
print("Maximum value:", knapsack_fractional(n, W))
