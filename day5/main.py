file = open("input.txt")
file = file.readlines()

def jump(arg1, p2=False):
    count = 0
    pos = 0
    while pos >= 0 and pos < len(arg1):
        #print(arg1)
        count += 1
        oldpos = pos
        mod = 1
        pos += arg1[oldpos]
        if p2 and (pos - oldpos) >= 3:
            mod = -1
        arg1[oldpos] += mod
    return count

assert jump([0,3,0,1,-3])==5
assert jump([0,3,0,1,-3], True)==10

nums = []
for num in file:
    nums.append(int(num))

c = jump(list(nums))
c2 = jump(list(nums), True)
print(c)
print(c2)
