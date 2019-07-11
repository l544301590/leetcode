# -*-coding:utf-8-*-
import sys
arr = sys.stdin.readline().strip().split(" ")
res, flag = [0, 0, 0, 0, 0, 0], True
nums = [
    [2, 1, 0],
    [3, 2, 1, 0],
    [5, 4, 3, 2, 1, 0],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [5, 4, 3, 2, 1, 0],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]
for i in range(6):
    for num in nums[i]:
        if str(num) in arr:
            res[i] = num
            arr.remove(str(num))
            break
    else:
        flag = False
        print("invalid")
        exit(0)
if flag:
    print(str(res[0]) + str(res[1]) + ":" + str(res[2]) + str(res[3]) + ":" + str(res[4]) + str(res[5]))

