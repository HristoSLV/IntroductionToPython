# Get the input string from the user
input_string = input()

# Check if the input string contains single quotes
if "'" in input_string:
    # If it does, enclose the string in double quotes
    output_string = '"' + input_string + '"'
else:
    # If it doesn't, enclose the string in single quotes
    output_string = "'" + input_string + "'"

# Print the output string
print(output_string)
