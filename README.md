# goit-algo-hw-08

Homework on Heaps

## What I Did

### Main Task - Minimize Cable Connection Cost

I solved the cable merging problem using a min heap from Python's `heapq` module. 

**File:** `task1.py`

**Problem:**
There are several network cables of different lengths that need to be merged together. The cost of connecting two cables equals the sum of their lengths. I need to find the order of merging that minimizes the total cost.

**My Solution:**
I used a greedy algorithm with a min heap: 
1. Put all cable lengths into a min heap
2. Always take the two shortest cables
3. Merge them (cost = sum of their lengths)
4. Put the merged cable back into the heap
5. Repeat until only one cable remains

**Why this works:**
The greedy approach of always merging the shortest cables first minimizes total cost because shorter cables get used in more merge operations. By merging them early, we minimize their contribution to the total cost.

**Example:**
For cables `[4, 3, 2, 6]`:
- Merge 2 + 3 = 5, cost = 5
- Merge 4 + 5 = 9, cost = 5 + 9 = 14
- Merge 6 + 9 = 15, cost = 14 + 15 = 29
- Total minimum cost = 29

If we merged them in a different order, the cost would be higher.

## How to Run

```bash
python3 task1.py
```

## Files
- `task1.py` - Cable merging problem solution
- `README.md` - This file

## Conclusion

Using a min heap makes this problem efficient.  The heap automatically keeps track of the shortest cables, so we don't need to sort the array after every merge. The time complexity is O(n log n) where n is the number of cables.

This greedy algorithm always gives the optimal solution because merging shorter cables first minimizes how many times their lengths are counted in the total cost.
