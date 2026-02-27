def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))