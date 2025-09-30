# Function to test if a number is Positive, Negative, or Zero
def check_num(n):
    # Define your if-statement here to check the value of n and return "Positive", "Negative", or "Zero"
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


# Testing your function with inputs
input_number = int(input())
# Remember to call the check_num function with a number as argument.
print(check_num(input_number))
