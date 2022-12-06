games = open("input.txt", "r")
score = 0
inputA = ["A", "B", "C"]
inputB = ["X", "Y", "Z"]
for line in games:
    linelist = line.split()
    if linelist[1] == "Y":
        score = score + inputA.index(linelist[0])+ 1 + 3
    if linelist[1] == "X":
        if linelist[0] == "A":
            score = score + 3
        if linelist[0] == "B":
            score = score + 1
        if linelist[0] == "C":
            score = score + 2
    if linelist[1] == "Z":
        if linelist[0] == "A":
            score = score + 2 + 6
        if linelist[0] == "B":
            score = score + 3 + 6
        if linelist[0] == "C":
            score = score + 1 + 6

    print(score)
