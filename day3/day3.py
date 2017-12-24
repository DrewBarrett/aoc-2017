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
    side = 3
    while current != input:
        mod = 0
        current -= 1
        if side == 3 or side == 2:
            mod = -1
        else:
            mod = 1
        if width > 1:
            x += mod
            width -= 1
            if width == 1:
                side -= 1
                height = nearest
        elif height > 1:
            y += mod
            height -= 1
            if height == 1:
                side -= 1
                width = nearest
    return abs(x) + abs(y)


assert nearestOddSquare(1) == 1
assert nearestOddSquare(8) == 3
assert distance(1) == 0
assert distance(12) == 3
assert distance(23) == 2
assert distance(1024) == 31

for line in file:
    print(distance(int(line)))

