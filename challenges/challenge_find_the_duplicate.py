def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False

    num_set = set()

    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        elif num in num_set:
            return num
        else:
            num_set.add(num)
    return False
