# Find the longest continuous subarray with unique elements (no duplicates).
def longest_unique(arr):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


arr = [1, 2, 3, 1, 2, 3, 4, 5]
result = longest_unique(arr)

print(result)  


# 2.Maximum Subarray (Kadane’s Algorithm)

def max_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example input
arr = [2, -1, 3, -2, 4]

# Call function
result = max_subarray(arr)

# Print output
print("Maximum Subarray Sum:", result)


##Q3: Rainwater Collection System
 #Problem Statement
#You are given heights of buildings in a row.
#After rain, water gets trapped between taller buildings.

# Your task:
#Calculate the total amount of water trapped.
def trap(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# Example
arr = [3, 0, 2, 0, 4]
print(trap(arr))


#Q4: Employee Performance Analysis
 # Problem Statement

#A company records an employee’s monthly performance scores.

#Scores can be positive (good performance)
#Or negative (bad performance)
def max_performance(arr):
    current_sum = arr[0]   # running sum
    max_sum = arr[0]       # best result

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        # choose best: start new OR continue

        max_sum = max(max_sum, current_sum)
        # update maximum

    return max_sum

# Example
arr = [5, -2, 3, 4, -1]
print(max_performance(arr))


# Q5: Product Sales Analysis
# Find maximum product of a continuous subarray

def max_product(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod  # swap

        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])

        result = max(result, max_prod)

    return result


# Example
arr = [2, 3, -2, 4]
print(max_product(arr))

# Q6: Customer Purchase History
# Find longest subarray with unique elements

def longest_unique(arr):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Example
arr = [1, 2, 3, 1, 2, 3, 4, 5]
print(longest_unique(arr))


# Q7: Bank Transaction Analysis
# Count subarrays with given sum

def count_subarrays(arr, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count


# Example
arr = [1, 2, 3, 2, 1]
k = 3
print(count_subarrays(arr, k))


# Q8: Employee Skill Grouping
# Group words with same characters

def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# Example
words = ["abc", "bca", "cab", "xyz", "zyx"]
print(group_anagrams(words))


# Q9: Network Packet Analysis
# Find longest consecutive sequence

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# Example
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))




# Q10: Hospital Appointment Scheduling
# Merge overlapping intervals

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        last = merged[-1]

        if intervals[i][0] <= last[1]:
            last[1] = max(last[1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged


# Example
intervals = [[1, 3], [2, 6], [8, 10]]
print(merge_intervals(intervals))