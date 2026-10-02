# 0/1 Knapsack Problem

# Get number of items
n = int(input("Enter number of items: "))

# Get weights
weights = list(map(int, input("Enter weights: ").split()))

# Get values
values = list(map(int, input("Enter values: ").split()))

# Check input size
if len(weights) != n or len(values) != n:
    print("Error: Number of weights and values must be", n)
    exit()

# Get bag capacity
capacity = int(input("Enter capacity: "))

# Create DP table
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

# Fill the table
for i in range(1, n + 1):

    for w in range(1, capacity + 1):

        # Check if item fits
        if weights[i - 1] <= w:

            # Take the item
            take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            # Skip the item
            skip = dp[i - 1][w]

            # Choose maximum
            dp[i][w] = max(take, skip)

        else:
            # Item does not fit
            dp[i][w] = dp[i - 1][w]


# Print maximum value
print("\nMaximum value:", dp[n][capacity])


# Find selected items
w = capacity
selected = []

for i in range(n, 0, -1):

    # Item was selected
    if dp[i][w] != dp[i - 1][w]:

        selected.append(i)

        # Reduce capacity
        w -= weights[i - 1]


# Reverse the list
selected.reverse()

print("Selected items:", selected)


# Calculate total weight
total_weight = 0

for i in selected:
    total_weight += weights[i - 1]

print("Total weight:", total_weight)