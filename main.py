from collections import defaultdict
from datetime import datetime,timedelta

personList = defaultdict(list)
file = open("3rdday","r")
for string in file:
    if 'Joined before' in string:
        string = string.split('Joined before')
    elif 'Joined' in string:
        string = string.split('Joined')
    elif 'Left' in string:
        string = string.split('Left')
    else:
        continue
    name = string[0].title().strip().split('(')[0]
    datetimeObject = datetime.strptime(string[1].replace(' ','').strip(),'%m/%d/%Y,%I:%M:%S%p')
    personList[name].append(datetimeObject)

timeTaken = {person:0 for person in personList}
outputFile = open("output.txt","w")
endTime = datetime.strptime("01/25/2021,8:45:0PM",'%m/%d/%Y,%I:%M:%S%p')
for person in personList:
    record = personList[person]
    time = timedelta(seconds=0)
    for idx in range(1,len(record),2):
        time += record[idx]-record[idx-1]
    if len(record)&1:
        time += endTime-record[-1]
    outputFile.write(person+" "*(40-len(person))+str(time)+"\n")
outputFile.close()
