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

assert checkLine("5\t1\t9\t5") == 8
assert checkLine("7\t5\t3") == 4
assert checkLine("2\t4\t6\t8") == 6

tot = 0
for line in file:
    tot += checkLine(line)
print(tot)