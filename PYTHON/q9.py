def remove_duplicates_keep_order(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(remove_duplicates_keep_order(lst))