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
for instruction in instructionlist:
    print(instruction)
    counter = int(instruction[0])
    print("amount to be moved: " + str(counter))
    print("moved from: " + str(stacks[int(instruction[1]) - 1]))
    print("moved to: " + str( stacks[int(instruction[2]) - 1]))
    while counter >= 1:
        counter = counter - 1
        moved = stacks[int(instruction[1]) - 1].pop(-(counter) - 1)
        print(moved)
        stacks[int(instruction[2]) - 1].append(moved)
    print("stack of origin, current state: " + str(stacks[int(instruction[1]) - 1]))
    print("stack of destination, current state: " + str( stacks[int(instruction[2]) - 1]))
result = ""
for stack in stacks:
    result = result + stack[-1]
print(result)
