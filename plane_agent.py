import sys
import math
prompt = []
map = []
f = ""
h = ""
fuel = 0
start = []
current = []
goal = []
row = 0

outputMapCounter = 0

# Reads file

def readFile():
    x = len(prompt)
    global f
    
    if(len(prompt) != 0):
        temp = prompt[0]
        
        if(temp == "weather.txt"):
            f = open(temp, "r")
            fl = f.readlines()
            readMap(fl)
        else:
            print("\nError: No such File Exist")
            print("Please check the file name")
    
    else:
        print("\nList is Empty") 

# Constructs a map from the given *.txt files
def readMap(fl):
    temp = ""
    
    for x in fl:
        #print(fl)
        temp = x
        line = temp[:len(x)]
#         print(line)
        findStartGoal(line)
        map.append(line)
    f.close()
#     print(map)
    print("row 1 has length:",len(map[0]), "\nrow 2 has length:", len(map[1]))
    
        
# Gets arguements from command line
# Includes: txt file, heuristic function(manhattan, euclidean or made up), intial fuel 
       
def getPrompt():
    x = len(sys.argv)
    i = 1
    for x in range(1, x):
        prompt.append(str(sys.argv[i]))
        i = i + 1
    return prompt

# Sepcifies what heuristic function to use for the given map

def setHeuristic():
    global h
    h = prompt[1]
    print(h)
    
    if(h == "manhattan"):
        manhattan()
    elif(h == "euclidean"):
        euclidean()
    elif(h == "made_up"):
        made_up()
    else:
        print("\nNo heuristic function was specified in list")
        print("Manhattan function is picked by defalut\n")
        manhattan()

def setFuel():
    global fuel 
    fuel = prompt[2]

    
### Calculations

# manhattan

def manhattan():
    print("this is manhattan distance")
    global distance
    distance = abs( (current[0] - goal[0] ) ) + abs( ( current[1] - goal[1]) ) 
    print(distance)
# euclidean

def euclidean():
    print("this is euclidean distance")
    global distance
    a = (current[0] - goal[0]) * (current[0] - goal[0]) 
    b = (current[1] - goal[1]) * (current[1] - goal[1])
    c = a + b
    distance = math.sqrt(c)
    distance = round(distance, 4)
    print(distance)
# made_up

def made_up():
    print("this is made up distance")
    

# Prints current map
def outputMap():
    global map
    global outputMapCounter
    outputMapCounter = outputMapCounter + 1
    f = open("outputMap.txt", "a+")
    f.write("\n\nThis is map: %d\r" % (outputMapCounter) )
    for x in range(0, len(map)):
#         print(map[x])
        f.write(map[x])
# finds the start of the airplane
    f.close()

def findStartGoal(line):
    list = ['A', 'B', 'C',
            'D', 'E', 'F', 
            'G', 'H', 'I']
    print(line)
    global row
    global start
    global goal
    pos = 0
    
    for j in range(0, len(line)):
        current = line[pos + j:pos + j + 1]
#         print(current)
        for k in range(0, len(list)):
#             test = list[k]
#             print(test)
            if(current == list[k]):
                #print("this is column:", j)
                start = [row, j]
#                 print(k)
#                 print(list[k])
#                 print("row = ", row)
#                 print("column =", j)
#             print("j = ", j)    
#             print("k = ", k)
        if(current == 'P'):
            goal = [row, j]
    row = row + 1  
    #print(f1)

# A* alogrithm

def A_starAlgorithm(map, start, goal):
    print("test")



# Clears map - for programmers use
def clearMap():
    global outputMapCounter
    outputMapCounter = 0
    f = open("outputMap.txt", "w+")
    f.write("")
    f.close()
    

####### Main #######

getPrompt()
if(len(prompt) > 0):
    readFile()
    print("Start:", start)
    print("Goal:", goal)
    print(map)
    outputMap()
    clearMap()  
    outputMap()
    #setHeuristic()
    #setFuel()
    #print(h)
    #outputMap()

