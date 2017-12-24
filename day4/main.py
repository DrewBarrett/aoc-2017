file = open("input.txt")
file = file.readlines()

def checkDup(arg1):
    words = arg1.split(" ")
    seen = []
    for word in words:
        if word not in seen:
            seen.append(word)
        else:
            return True
    return False
    

assert checkDup("aa bb cc dd ee")==False
assert checkDup("aa bb cc dd aa")==True
assert checkDup("aa bb cc dd aaa")==False


valid = 0

for line in file:
    if not checkDup(line.strip()):
        valid += 1

print(valid)
