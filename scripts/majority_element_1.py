
num_list = [1,3,4,2,2,2,1,2,2,2]

num_map = {}
for i in num_list:
    if i in num_map:
        num_map[i] = num_map[i] + 1
    else:
        num_map[i] = 1

for num, counts in num_map.items():
    if counts > len(num_list) // 2:
        print(num)



