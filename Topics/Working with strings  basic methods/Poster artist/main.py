def format_phone_number(phone):
    cleaned = ''.join(char for char in phone if char.isdigit())
    if len(cleaned) == 10:
        return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}\n"
    else:
        return "invalid phone number\n"


print(format_phone_number("123-456-7890"))
# Output: (123) 456-7890

print(format_phone_number("12345"))
# Output: invalid phone number
