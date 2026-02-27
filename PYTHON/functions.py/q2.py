def is_palindrome(s: str) -> bool:
    return s == s[::-1]
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")