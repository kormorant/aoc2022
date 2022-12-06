from functools import reduce
elflijst = open("input.txt", "r")
elfenencalorien = []
calorien = 0
for line in elflijst:
    if line.isspace():
        elfenencalorien.append(calorien)
        calorien = 0
    if line.strip().isdigit():
        calorien = calorien + int(line)
print(elfenencalorien)
b = 0
a = reduce(max, elfenencalorien)
print(a)
b = a
elfenencalorien.remove(a)
a = reduce(max, elfenencalorien)
print(a)
b = b + a
elfenencalorien.remove(a)
a = reduce(max, elfenencalorien)
print(a)
b = b + a
elfenencalorien.remove(a)
print(b)