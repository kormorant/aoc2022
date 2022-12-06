stacks = [['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],['S', 'W', 'C'],['R', 'Z', 'T', 'M'],['D', 'T', 'C', 'H','S', 'P', 'V'],['G', 'P', 'T', 'L', 'D', 'Z'],['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],['L', 'H', 'R', 'B', 'T', 'V', 'M'],['Q', 'P', 'D', 'S', 'V']]
instructionsbase = open("instructions.txt", "r")
instructionlist = []
print(stacks)
for instruction in instructionsbase:
    instruction = instruction.split()
    for part in instruction:
        if part.isdigit():
            pass
        else:
            instruction.remove(part)
    instructionlist.append(instruction)
    #print(instructionlist)
for instruction in instructionlist:
    counter = int(instruction[0])
    print("entire collection:")
    print("stack 1 " + str(stacks[0]))
    print("stack 2 " + str(stacks[1]))
    print("stack 3 " + str(stacks[2]))
    print("stack 4 " + str(stacks[3]))
    print("stack 5 " + str(stacks[4]))
    print("stack 6 " + str(stacks[5]))
    print("stack 7 " + str(stacks[6]))
    print("stack 8 " + str(stacks[7]))
    print("stack 9 " + str(stacks[8]))
    print("instruction:")
    print(instruction)
    print("stack content:")
    print(stacks[int(instruction[1]) - 1])
    while counter >= 1:
        counter = counter - 1
        moved = stacks[int(instruction[1]) - 1].pop(-1)
        print(moved)
        stacks[int(instruction[2]) - 1].append(moved)
result = ""
for stack in stacks:
    result = result + stack[-1]
print(result)
