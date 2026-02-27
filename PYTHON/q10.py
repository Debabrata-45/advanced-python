def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
s = input("Enter a string: ")
print(string_length(s))