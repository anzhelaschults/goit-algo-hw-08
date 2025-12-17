import heapq

def minimize_cable_cost(cables):

    # Create a min heap from the cables
    heapq.heapify(cables)
    
    total_cost = 0
    
    print("Initial cables:", cables)
    print("\nMerging process:")
    
    while len(cables) > 1:
  
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        merge_cost = first + second
        total_cost += merge_cost
        
        print(f"  Merge {first} + {second} = {merge_cost}, Total cost so far: {total_cost}")
        
        heapq. heappush(cables, merge_cost)
    
    return total_cost

# Test the function
if __name__ == "__main__":
    print("=== Cable Merging Problem ===\n")
    
    # Example 1
    cables1 = [4, 3, 2, 6]
    print("Example 1:")
    result1 = minimize_cable_cost(cables1.copy())
    print(f"\nMinimum total cost: {result1}")
    print("="*50)
    
    # Example 2
    print("\nExample 2:")
    cables2 = [1, 2, 3, 4, 5]
    result2 = minimize_cable_cost(cables2.copy())
    print(f"\nMinimum total cost: {result2}")
    print("="*50)
    
    # Example 3
    print("\nExample 3:")
    cables3 = [5, 4, 2, 8]
    result3 = minimize_cable_cost(cables3.copy())
    print(f"\nMinimum total cost: {result3}")
    print("="*50)
    
    print("\n### Explanation ###")
    print("The algorithm always merges the two shortest cables first.")
    print("This greedy approach minimizes the total cost because:")
    print("  - Shorter cables are used in more merge operations")
    print("  - By merging them early, we minimize their contribution to total cost")