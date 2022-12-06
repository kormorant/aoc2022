bufferinput = open("input.txt", "r")
position = 0
bufferlist = []
for line in bufferinput:
    for character in line:
        bufferlist.append(character)
print(bufferlist)
counter = 1
result = 0
resultlist = []
for cc in bufferlist:
    listoffourteen = []
    n = 0
    listoffourteen.append(cc)
    while n < 13 and int(counter + n) < len(bufferlist):
        #print(n)
        currentchar = bufferlist[counter + n]
        if currentchar not in listoffourteen:
            listoffourteen.append(currentchar)
        n = n + 1
    if len(listoffourteen) == 14:
        print(counter)
        print("this is the one")
        result = counter
        resultlist = listoffourteen
    counter = counter + 1
    print(counter)
    print(listoffourteen)
    print(len(listoffourteen))
print("")
print(result)
print(resultlist)
print(len(resultlist))
print("".join(resultlist))
