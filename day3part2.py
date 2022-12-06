rucksacks = open("input.txt", "r")
alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
common = []
score = 0
counter = 0
threes = []
placeletter = []
for rucksack in rucksacks:
    placesack = rucksack[:-1] # remove newline
    threes.append(placesack) # add string to group of three
    print(threes) # debug line
    counter = counter + 1 # increase counter by 1
    print(counter) # debug line
    if counter == 3:
        for letter in threes[0]:
            if letter in threes[1] and letter in threes[2]: # check if letter from first group exists in second and third groups
                placeletter.append(letter) # add letter to letter placeholder list
                print(letter) # debug line
        counter = 0 # reset counter
        threes = [] # reset group of three
        if len(placeletter) > 0: 
            common.append(placeletter[0]) # add letter to common list, this to prevent the addition of duplicate letters.
        placeletter = [] # reset placeholder letter list
print(common) # debug line
for x in common:
    score = score + alfabet.find(x) + 1 # increase score, based on the position of the letter in the alfabet string. The plus 1 is because of zero-indexing.
print(score)
print(len(common)) # debug line
