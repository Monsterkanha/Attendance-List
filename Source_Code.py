
fhandle = open("2ndday")
ans = []
for line in fhandle:
    line.strip()
    line = line.lower()

    if("Joined" in line):
        line = line.split("Joined" or "joined")
    else:
        line = line.split("Left" or "left")

    ans.append(line[0])
ans= list(set(ans))
ans.sort()
for i in ans:
    print(i,end="")
