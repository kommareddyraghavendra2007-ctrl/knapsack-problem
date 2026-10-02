# 0/1 Knapsack Problem

A Python implementation of the **0/1 Knapsack Problem** using **Dynamic Programming**.

## 📌 Problem Statement

The 0/1 Knapsack Problem is an optimization problem where we are given:

* A set of `n` items
* A weight for each item
* A value for each item
* A knapsack with a limited capacity

The goal is to select items such that:

1. The total weight does not exceed the knapsack capacity.
2. The total value of the selected items is maximum.
3. Each item can be selected **only once**.

The term **0/1** means that an item can either be:

* `0` → Not selected
* `1` → Selected

An item cannot be partially selected.

---

## 🎯 What Problem Did We Solve?

Suppose we have several items, each with a different weight and value, but our bag can carry only a limited weight.

For example:

| Item | Weight | Value |
| ---- | ------ | ----- |
| 1    | 2      | 3     |
| 2    | 3      | 4     |
| 3    | 4      | 5     |
| 4    | 5      | 6     |

If the knapsack capacity is `5`, we need to find which items should be selected to obtain the maximum value.

The optimal selection is:

* Item 1 → Weight `2`, Value `3`
* Item 2 → Weight `3`, Value `4`

Total weight:

```text
2 + 3 = 5
```

Total value:

```text
3 + 4 = 7
```

Therefore, the maximum possible value is **7**.

---

## 💡 How Did We Solve It?

We solved the problem using **Dynamic Programming (DP)**.

Instead of trying every possible combination of items, we divide the problem into smaller subproblems and store their results.

We create a DP table:

```text
dp[i][w]
```

where:

* `i` = number of items considered
* `w` = current available capacity
* `dp[i][w]` = maximum value possible using the first `i` items with capacity `w`

For every item, we have two choices:

### 1. Take the item

If the item fits inside the knapsack:

```text
Take = item value + best value for remaining capacity
```

### 2. Skip the item

We can also choose not to take it:

```text
Skip = best value without the current item
```

We then choose the better option:

```text
dp[i][w] = max(Take, Skip)
```

If the item does not fit, we simply use the previous result.

---

## 🧠 Why Did We Choose Dynamic Programming?

We chose Dynamic Programming because the 0/1 Knapsack Problem contains **overlapping subproblems** and has **optimal substructure**.

A brute-force approach checks every possible combination of items. For `n` items, this can require:

```text
O(2ⁿ)
```

operations, which becomes very expensive as the number of items increases.

Dynamic Programming avoids calculating the same subproblems repeatedly by storing previously calculated results.

### Advantages

* Avoids repeated calculations
* Much faster than brute force for moderate capacities
* Easy to implement using a DP table
* Guarantees the optimal solution
* Clearly demonstrates an important algorithmic optimization technique

---

## 🔄 Algorithm

```text
1. Start
2. Read the number of items
3. Read the weights of the items
4. Read the values of the items
5. Read the knapsack capacity
6. Create a DP table initialized with 0
7. For every item:
      For every possible capacity:
          If the item fits:
              Calculate Take value
              Calculate Skip value
              Store the maximum
          Otherwise:
              Copy the previous value
8. The last cell contains the maximum value
9. Trace the table backwards to find selected items
10. Calculate total weight
11. Display the result
12. Stop
```

---

## ⏱️ Complexity

Let:

* `n` = number of items
* `W` = knapsack capacity

### Time Complexity

```text
O(n × W)
```

The algorithm processes every item for every possible capacity.

### Space Complexity

```text
O(n × W)
```

The current implementation uses a two-dimensional DP table.

### Space-Optimized Version

A one-dimensional DP array can reduce the space complexity to:

```text
O(W)
```

while maintaining the same time complexity:

```text
O(n × W)
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Dynamic Programming**
* **Command Line / Terminal**

No external libraries are required.

---

## 📂 Project Structure

```text
0-1-knapsack/
│
├── knapsack.py
└── README.md
```

---

## ▶️ How to Execute

### Step 1: Install Python

Make sure Python 3 is installed on your system.

Check the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project folder:

```bash
cd 0-1-knapsack
```

### Step 3: Run the Program

On Windows:

```bash
python knapsack.py
```

On Linux/macOS:

```bash
python3 knapsack.py
```

---

## ⌨️ Input Format

The program accepts input through the terminal.

```text
Enter number of items: 4
Enter weights: 2 3 4 5
Enter values: 3 4 5 6
Enter capacity: 5
```

The number of weights and values must match the number of items.

For example:

```text
Number of items = 4
Weights = 4 values
Values = 4 values
```

---

## 📤 Output

For the above input:

```text
Maximum value: 7
Selected items: [1, 2]
Total weight: 5
```

This means the program selected Item 1 and Item 2.

Their combined weight is:

```text
2 + 3 = 5
```

Their combined value is:

```text
3 + 4 = 7
```

---

## 🧪 Example

### Input

```text
Enter number of items: 4
Enter weights: 2 3 4 5
Enter values: 3 4 5 6
Enter capacity: 5
```

### Output

```text
Maximum value: 7
Selected items: [1, 2]
Total weight: 5
```

---

## 🌍 Real-World Applications

The 0/1 Knapsack concept can be applied to:

* Resource allocation
* Budget planning
* Project selection
* Investment selection
* Cargo loading
* Storage optimization
* Selecting tasks under limited resources

---

## 🚀 Future Improvements

Possible improvements to the project include:

* Graphical user interface
* Visualization of the DP table
* Step-by-step algorithm animation
* Comparison with brute-force and other approaches
* Space-optimized implementation
* Support for larger datasets
* Performance comparison between different algorithms

---

## 📚 Key Learning

This project demonstrates how **Dynamic Programming** can transform an expensive combinatorial problem into a more manageable solution by storing and reusing results from smaller subproblems.

The main idea is simple:

```text
For every item:
       ↓
Can we take it?
   ↙       ↘
 YES       NO
  ↓         ↓
Take      Skip
  ↓         ↓
Compare both
      ↓
Choose maximum
```

---

## 👨‍💻 Conclusion

The project successfully solves the **0/1 Knapsack Problem** using Dynamic Programming. The solution finds the maximum possible value while ensuring that the total weight remains within the given capacity.

The implementation accepts input directly from the terminal, calculates the optimal value, identifies the selected items, and displays the total weight.

**Algorithm:** Dynamic Programming
**Time Complexity:** `O(n × W)`
**Space Complexity:** `O(n × W)`
**Space-Optimized Complexity:** `O(W)`
