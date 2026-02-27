def reverse_string(s: str) -> str:
    rev = ""
    for ch in s:
        rev = ch + rev   # add current char in front
    return rev

# Example
text = input("Enter a string: ")
print("Reversed:", reverse_string(text))