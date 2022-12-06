bufferinput = open("input.txt", "r")
position = 0
bufferlist = []
for line in bufferinput:
    for character in line:
        bufferlist.append(character)
fours = []
for character in bufferlist:
    position = position + 1
    if len(fours) == 4:
        placeholder = []
        for cc in fours:
            if cc not in placeholder:
                placeholder.append(cc)
        if len(placeholder) == 4:
            position = position - 4
            break
        fours = []
    fours.append(character)
print(position)
