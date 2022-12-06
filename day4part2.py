assignments = open("input.txt", "r")
score = 0
for assignmentpair in assignments:
    overlap = False
    assignmentpair = assignmentpair[:-1] # remove newline
    pairs = assignmentpair.split(",") # split pair into individual assignments
    firstpair = []
    secondpair = []
    for pair in pairs:
        pair = pair.split("-")
        #print(pair)
        if firstpair == []:
            firstpair.append(int(pair[0]))
            counter = int(pair[0]) + 1
            while counter <= int(pair[1]):
                firstpair.append(counter)
                counter = counter + 1
        elif firstpair != []:
            secondpair.append(int(pair[0]))
            counter = int(pair[0]) + 1
            while counter <= int(pair[1]):
                secondpair.append(counter)
                counter = counter + 1
    print(firstpair)
    print(secondpair)
    #print(pairs) # debug line
    for number in firstpair:
        if number in secondpair:
            overlap = True
    if overlap:
        score = score + 1
print(score)
