import sys
import math

list = ['P','A','B','C','D',
        'E','F','G','H','I']

prompt = []
map = []
f = ""
h = ""
fuel = 0
start = []
# current = []
goal = []
oList = []
cList = []
numCol = 0
numRow = 0
outputMapCounter = 0

# Reads file

def readFile():
    
    global f

    x = len(prompt)
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
    global numCol
   
    for x in fl:
        #print(fl)
        temp = x
        line = temp[:len(x)]
        
#         print(line)
        findStartGoal(line)
        map.append(line)
    f.close()
#     print(map)
    numCol = len(map[0]) - 1
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

def setHeuristic(current, goal):
    global h
    h = prompt[1]
    #print(h)
    distance = 0
    
    if(h == "manhattan"):
        distance = manhattan(current, goal)
    elif(h == "euclidean"):
        distance = euclidean(current, goal)
    elif(h == "made_up"):
        distance = made_up()
    else:
        print("\nNo heuristic function was specified in list")
        print("Manhattan function is picked by defalut\n")
        manhattan(current, goal)
    return distance

# sets Fuel

def setFuel():
    global fuel 
    fuel = prompt[2]

# sets g_value cost to move to square

def setG_value():
    global list
    

### Calculations

# manhattan

def manhattan(current, goal):
    global distance
    distance = abs( (current[0] - goal[0] ) ) + abs( ( current[1] - goal[1]) ) 
    #print("this is manhattan distance: ", distance)
    return distance
# euclidean

def euclidean(current, goal):
    print("this is euclidean distance")
    global distance
    a = (current[0] - goal[0]) * (current[0] - goal[0]) 
    b = (current[1] - goal[1]) * (current[1] - goal[1])
    c = a + b
    distance = math.sqrt(c)
    distance = round(distance, 4)
    print(distance)
    return distance
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

# Prints map onto console window
def printMap():
    global map
    for x in range(0, len(map)):
        print(map[x], end="")     # prints w/o newline
    print("\n")
    
# Finds the position of the Start and goal in map
def findStartGoal(line):
    global list
    print(line)
    global numRow
    global start
    global goal
    pos = 0
    
    for j in range(0, len(line)):
        current = line[pos + j:pos + j + 1]
#         print(current)

        for k in range(1, len(list)):
#             test = list[k]
#             print(test)
            if(current == list[k]):
                #print("this is column:", j)
                start = [numRow, j]
#                 print(k)
#                 print(list[k])
#                 print("row = ", row)
#                 print("column =", j)
#             print("j = ", j)    
#             print("k = ", k)
        if(current == list[0]):
            goal = [numRow, j]
    numRow = numRow + 1  
    print(numRow)
    #print(f1)
   
# A* alogrithm

def A_starAlgorithm(node):
    global map
    max_f = 0;
    node["neighbors"] = getNeighbors(node)
 #   print(node["neighbors"])
    child = node.get("neighbors")
    
    for x in range(0, len(child)):
        temp = child[x]
        newParent = node["parent"]
        temp["parent"] = newParent
        
        index = newParent
        test = valueOnMap(index)
        temp["g_value"] = test
        temp["h_value"] = setHeuristic(temp["pos"], goal)
        temp["f_value"] = temp["g_value"] + temp["h_value"]
        temp["fuel"] = valueOnMap(temp["pos"])
        min_f = temp["f_value"]
        if(min_f > max_f):
            max_f = min_f
        
        
        print(temp)
        #print(max_f)

    
       # print(valueOnMap())
        
# Gets index and finds the value on the map

def valueOnMap(index):
 #   index = [0, 0]
    global list
    row = index[0]
    col = index[1]
    
    y = map[row]
    x = y[col]
    
    if(x.isalpha()):
        value = list.index(x)
    else:
        value = int(x)
#     for x in list:
#         if(x == y[col]):
#             value = list.index(x)
#             print(value)
#         counter = counter + 1
        
    #print(value)
    return value

# creates a NODE

def node(map, current):
    node = {"pos" : current,
            "parent": [],
            "neighbors": [] ,
            "h_value": 0,
            "g_value": 0,
            "f_value": 0,
            "fuel" : 0,
            "map" : [map]}
       
    return node

# Functions gets neighbors according to heuristic picked
    
def getNeighbors(current):
    global lenCol
    global lenRow
    global f
    global oList
    index = current["pos"]
    print("index", index)
    list = []
    top = index[0] - 1
    center = index[0]
    bottom = index[0] + 1
    
    if(top >= 0):
        if(f == "manhattan"):
            list.append(top,index[1])
        else:
            temp = getLeftRight(top,index)
            for x in temp:
                list.append(x)
    
    
    temp = getLeftRight(center, index)
    for x in temp:
        list.append(x)
    

    if(bottom <= numRow):
        if(f == "manhattan"):
            list.append(top,index[1])
        else:    
            temp = getLeftRight(bottom, index)    
            for x in temp:
                list.append(x)
    
    newList = []
    for x in list:
        child = x
        oList.append(child)
        newList.append(node(map, x))
     
     
#     
#     for y in test:
#         print(y)
    return newList

# Functions that get left and right neighbors

def getLeftRight(center, index):
    global f
    child = []
    left = index[1] - 1
    right = index[1] + 1
    
    if(left >= 0):
        temp = [center, left]
        child.append(temp)
    
    if(center != index[0]):
        temp = [center, index[1]]
        child.append(temp)
    
    if(right < numCol):
        temp = [center, right]
        child.append(temp)
    
    
    print("These are children: ",child)

    
    return child 
        

#     print("where are the neighbors: ", h)
#     if(h == "manhattan"):
#         

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
    setFuel()
    printMap()
   
if not oList:
    print("\nnothin in list")
    root = node(map, start)
    root["parent"] = start
    root["g_value"] = 0
    root["h_value"] = setHeuristic(start, goal)
    root["f_value"] = root["g_value"] + root["h_value"]
    root["fuel"] = fuel
    cList.append(root)
    print(root)
    A_starAlgorithm(root)
    #setHeuristic()
    #setFuel()
    #print(h)
    #outputMap()

