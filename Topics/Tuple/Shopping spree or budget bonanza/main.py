# Function to process product information and calculate total cost
def calculate_total_cost(product_info):
    # Your code here
    name, price, quantity = product_info
    total_cost = float(price) * int(quantity)
    return f'{name}: Total cost = ${total_cost:.2f}'

# Read input and split into a tuple
input_string = input().strip()
product_tuple = tuple(input_string.split())

# Call the function and print the result
result = calculate_total_cost(product_tuple)
print(result)