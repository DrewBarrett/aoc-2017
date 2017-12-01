file = open("input.txt")
file = file.readlines()

add = []
addHalfway = []

for line in file:
    line = line.strip()
    for i in range(0, len(line)):
        k = i + 1
        j = i + (len(line)/2)
        k %= len(line)
        j %= len(line)
        if line[i] == line[k]:
            add.append(int(line[i]))
        if line[i] == line[j]:
            addHalfway.append(int(line[j]))

print(sum(add), sum(addHalfway))
