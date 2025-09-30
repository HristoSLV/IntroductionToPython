# Read input list of integers
nums = list(map(int, input().split()))

# Read the index
index = int(input())

# Print the integer at the specified index
# Start your code below
if index < len(nums):
    print(nums[index])
else:
    print("Index out of range")
