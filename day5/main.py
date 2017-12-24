file = open("input.txt")
file = file.readlines()

def jump(arg1):
    count = 0
    pos = 0
    while pos >= 0 and pos < len(arg1):
        #print(arg1)
        count += 1
        oldpos = pos
        pos += arg1[oldpos]
        arg1[oldpos] += 1
    return count

assert jump([0,3,0,1,-3])==5

nums = []
for num in file:
    nums.append(int(num))
c = jump(nums)
print(c)
