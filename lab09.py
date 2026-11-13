# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)

    return best_profit


def max_subarray(nums):
    if not nums:
        return 0

    max_subarray_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_subarray_sum = max(max_subarray_sum, current_sum)

    return max_subarray_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Use a stack to match each closing bracket with the most recent opening bracket.
    #   If the stack is empty or mismatched, return False.
    #   Return True only if all brackets are matched.
    pass

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
