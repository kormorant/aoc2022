assignments = open("input.txt", "r")
score = 0
for assignmentpair in assignments:
    assignmentpair = assignmentpair[:-1] # remove newline
    pairs = assignmentpair.split(",") # split pair into individual assignments
    # print(pairs) # debug line
    positions = []
    for assignment in pairs:
        positions.append(assignment.split("-")) # split into individual positions
    print(positions) # debug line
    if int(positions[0][0]) >= int(positions[1][0]) and int(positions[0][1]) <= int(positions[1][1]):
            score = score + 1 # then one assignment of this pair is completelty inside the other
            print("first within second")
    elif int(positions[1][0]) >= int(positions[0][0]) and int(positions[1][1]) <= int(positions[0][1]):
            score = score + 1 # then one assignment of this pair is completely inside the other
            print("second within first")
print(score) # show score

