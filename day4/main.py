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

def checkAna(arg1):
    words = arg1.split(" ")
    for word in words:
        for word2 in words:
            if word2 != word and len(word2) == len(word):
                ana = True
                for letter in word2:
                    if word2.count(letter) != word.count(letter):
                        ana = False
                if ana:
                    return True
    return False

assert checkDup("aa bb cc dd ee")==False
assert checkDup("aa bb cc dd aa")==True
assert checkDup("aa bb cc dd aaa")==False
assert checkAna("abcde fghij")==False
assert checkAna("abcde xyz ecdab")==True
assert checkAna("a ab abc abd abf abj")==False
assert checkAna("iiii oiii ooii oooi oooo")==False
assert checkAna("oiii ioii iioi iiio")==True

valid = 0
valid2 = 0
for line in file:
    if not checkDup(line.strip()):
        valid += 1
    if not checkDup(line.strip()) and not checkAna(line.strip()):
        valid2 += 1

print(valid)
print(valid2)
