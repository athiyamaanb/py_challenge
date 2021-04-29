# Top two numbers occur most
# Output - [5,7] or [7,5]
s = [5,5,5,6,7,7,10]
n = 2 # Top two numbers occur most


########################################################
# Method 1
# find number of occurance for each distict element
int_map = {}
for i in s:
    int_map[i] = int_map[i] + 1 if i in int_map else 1
# print(int_map)

# Using Sort
sorted_int_map = sorted(int_map.items(), key=lambda item: item[1], reverse=True)
print("with sort")
print([k for k, _ in sorted_int_map[:n]])
########################################################

########################################################
# Method 2
# Using Collections
import collections
cnt = collections.Counter(s)
print("with collections")
print([k for k, _ in cnt.most_common(2)])
########################################################


########################################################
# Method 3
# Without collections and without sort
int_map = {}
for i in s:
    int_map[i] = int_map[i] + 1 if i in int_map else 1
# print(int_map)

rev_int_map = {}
for k, v in int_map.items():
    rev_int_map[v] = rev_int_map[v] + [k] if v in rev_int_map else [k]

# print(rev_int_map)

sorted_int_map = []
for num in range(len(s), -1, -1):
    if num in rev_int_map:
        if len(sorted_int_map) == n:
            break
        else:
            sorted_int_map = sorted_int_map + rev_int_map[num]
print("Without inbuilt sort")
print(sorted_int_map)

########################################################
