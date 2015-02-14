#print("this did something")
import sys

# Function gets txt file, heuristic function(manhattan, euclidean or made up), intial fuel 
# list - is a list with the for the following 
def getPrompt(x):
    list = []
    i = 1
    for x in range(1, x):
        list.append(str(sys.argv[i]))
        i = i + 1
    
    return list
