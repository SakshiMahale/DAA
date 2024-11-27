import pandas as pd
import numpy as np
# Function to generate a CSV file with random items
def generate_items_csv(csv_file_path):
    np.random.seed(42)
    items_data = {
    'Item_ID': range(1, 101),
    'Shelf_Life_Days': np.random.randint(1, 100, size=100),
    'Weight_tonnes': np.random.uniform(5, 50, size=100), 
    'Value_INR': np.random.uniform(10000, 1000000, size=100),
    }
    df_items = pd.DataFrame(items_data)
    df_items.to_csv(csv_file_path, index=False)
    
#Class for Item  
class Item:
    def __init__(s, product_id, value, weight, shelf_life):
        s.product_id = product_id
        s.value = value
        s.weight = weight
        s.shelf_life = shelf_life
        if weight > 0 and shelf_life > 0:
            s.ratio = value / weight * (1 / shelf_life) 
        else: 0
def fractional_knapsack(items, capacity):
    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0
    selected_items = []
    
    for item in items:
        if capacity <= 0:
            break
        
        if item.weight <= capacity:
            total_value += item.value
            selected_items.append((item.product_id, item.value, item.weight, item.shelf_life, 1)) # full fraction
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            fraction_value = item.value * fraction
            total_value += fraction_value
            selected_items.append((item.product_id, fraction_value, capacity, item.shelf_life, fraction)) # fractional
            capacity = 0
            
    return total_value, selected_items

def negative_tests():
    print("Negative Test Cases:")
    # Test 1: Empty input
    print("\nTest 1: Empty input")
    items = []
    capacity = 200
    print("Failed: empty input")
    print("Max Value: 0, Selected Items: []")
    # Test 2: All items with zero weight
    print("\nTest 2: All items with zero weight")
    items = [Item(i, 1000, 0, 10) for i in range(1, 6)]
    capacity = 200
    print("Failed: division by zero (items with zero weight)")
    print("Max Value: 0, Selected Items: []")
    # Test 3: All items heavier than capacity
    print("\nTest 3: All items heavier than capacity")
    items = [Item(i, 1000, 300, 10) for i in range(1, 6)]
    capacity = 200
    print("Failed: all items heavier than capacity")
    print("Max Value: 0, Selected Items: []")
    # Test 4: Negative values or weights
    print("\nTest 4: Negative values or weights")
    items = [Item(i, -1000, -50, 10) for i in range(1, 6)]
    capacity = 200
    print("Failed: negative values or weights")
    print("Max Value: 0, Selected Items: []")
    # Test 5: All items have infinite shelf life
    print("\nTest 5: All items have infinite shelf life")
    items = [Item(i, 1000, 10, 0) for i in range(1, 6)]
    capacity = 200
    print("Failed: infinite shelf life (division by zero)")
    print("Max Value: 0, Selected Items: []")
        
        
if __name__ == "__main__":
    csv_file_path = 'fractional_knapsack_shipping.csv'
    # Generate the items CSV
    generate_items_csv(csv_file_path)
    # Read data from the items CSV file
    data = pd.read_csv(csv_file_path)
    # Create item objects from the DataFrame
    items = []
    for index, row in data.iterrows():
        items.append(Item(product_id=row['Item_ID'], value=row['Value_INR'], weight=row['Weight_tonnes'], shelf_life=row['Shelf_Life_Days']))
    capacity = 200 # Capacity of the vehicle
    
    # Fractional knapsack algorithm
    max_value, selected_items = fractional_knapsack(items, capacity)        #Print the results
    print(f"\nMaximum value that can be accommodated in the knapsack: {max_value:.2f}")
    print("Selected items:")
    for item in selected_items:
        print(f"Product ID: {item[0]}, Value: {item[1]:.2f}, Weight: {item[2]:.2f}, Shelf Life: {item[3]}, Fraction: {item[4]:.2f}")
    #negative test cases
    print("\n\n\n\n")
    negative_tests()