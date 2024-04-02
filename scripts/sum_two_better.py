

def sum_two(nums, target):
    visited = {}

    for i, num in enumerate(nums):
        if target - num in visited:
            return visited[target-num], i
        else:
            visited[num] = i




print(sum_two([2,11,7,15,100,300], 111))