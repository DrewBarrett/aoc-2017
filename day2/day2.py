file = open("input.txt")
file = file.readlines()

def checkLine(line):
    smallest = None
    largest = 0
    nums = line.split("\t")
    for num in nums:
        num = int(num)
        if smallest == None or num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest

def checkDiv(line):
    nums = line.split("\t")
    tot = 0
    for num in nums:
        nums.remove(num)
        num = int(num)
        
        for num2 in nums:
            num2 = int(num2)
            if num % num2 == 0:
                tot += (num / num2)
        nums.insert(0,str(num))
    return tot

assert checkLine("5\t1\t9\t5") == 8
assert checkLine("7\t5\t3") == 4
assert checkLine("2\t4\t6\t8") == 6

assert checkDiv("5\t9\t2\t8") == 4
assert checkDiv("9\t4\t7\t3") == 3
assert checkDiv("3\t8\t6\t5") == 2

tot = 0
tot2 = 0
for line in file:
    tot += checkLine(line)
    tot2 += checkDiv(line)
print(tot)
print(tot2)