import sys
import pprint
StoreProcess = []
logicalClock = {}
TimeStamp = {}

def addProcess():
    pName = input("Enter Processes Name separated by space  ")
    processList = pName.split()
    for process in processList:
        logicalClock[process] = [0]*len(processList)
        StoreProcess.append(process)

def sendMessage(t):
    eName = input("Enter the event which will recieve the message ")
    pName = input("Enter the process on which this event will occur ")
    if eName not in TimeStamp:
        TimeStamp.update({eName:t.copy()})
    position = StoreProcess.index(pName)
    if t[position]>logicalClock[pName][position]:
        logicalClock[pName][position] = t[position]
    TimeStamp[eName][position] = logicalClock[pName][position] + 1
    temp = TimeStamp[eName]
    logicalClock[pName] = temp.copy()

def addEvent():
    pName = input("Enter the process for which you want to add an event ")
    eName = input("Enter Event Name ")
    eType = input("Enter the type of event(normal/message) ")
    position = StoreProcess.index(pName)
    temp = logicalClock[pName]
    if eName not in TimeStamp:
        TimeStamp.update({eName:temp.copy()})
    if eType == "normal":
        TimeStamp[eName][position] = logicalClock[pName][position] + 1
        logicalClock[pName][position] += 1
    if eType == "message":
        TimeStamp[eName][position] = logicalClock[pName][position] + 1
        logicalClock[pName][position] += 1 
        tempo = TimeStamp[eName]
        sendMessage(tempo)

def display():
    pprint.pprint(TimeStamp)

if __name__ == "__main__":
    addProcess()
    while(1):
        print("1. ADD EVENT\n2. DISPLAY TIMESTAMP\n3. EXIT")
        n = int(input("Enter your choice  "))
        if n==1:
            addEvent()
        elif n==2:
            display()
        else:
            sys.exit("Bye Bye")

