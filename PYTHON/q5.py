def largest_in_list(nums):
    if not nums:
        return None

    largest = nums[0]
    for x in nums[1:]:
        if x > largest:
            largest = x
    return largest
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Largest number is:", largest_in_list(nums))