file = open("input.txt")
file = file.readlines()

def nearestOddSquare(num): # actually finds the smallest one larger than num
    i = 0
    while True:
        i += 1
        if i % 2 != 0:
            j = i * i
            if j >= num:
                return i


def distance(input):
    nearest = nearestOddSquare(input)
    x = (nearest - 1) / 2
    y = x
    width = nearest
    height = nearest
    current = nearest * nearest
    while current != input:
        current -= 1
        if width > 1:
            x -= 1
            width -= 1
        elif height > 1 :
            y -= 1
            height -= 1
        else:
            x += 1
    return abs(x) + abs(y)


assert nearestOddSquare(1) == 1
assert nearestOddSquare(8) == 3
assert distance(1) == 0
assert distance(12) == 3
assert distance(23) == 2
assert distance(1024) == 31

for line in file:
    print(line)