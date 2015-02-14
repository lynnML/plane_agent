HW#1 --- last modified Wednesday, 04-Feb-2015 15:02:36 PST.

Solution set.

Due date: Feb 11

Files to be submitted:
  Hw1.zip
Purpose: To gain experience with problem solving agents and the A⋆ algorithm

Related Course Outcomes:

The main course outcomes covered by this assignment are:

LO1 -- By code or by hand find solution nodes in a state space using the A⋆ algorithm.

Specification:

For this homework, you will build an airplane navigating in python that uses the A⋆ algorithm. 
Your python code should conform to the Pep8 coding guidelines and should work if Python 2.7.* 
is being used. You can work in teams of up to three people. 
Your program will be run from the command line with a line like:

python plane_agent.py file_name heuristic fuel

Here file_name is the name of a file which contains weather map drawn using ASCII character 
graphics; heuristic is one of the words manhattan, euclidean, or made_up. Finally, fuel is 
a positive integer. A weather map consists of a sequence of lines each made up of a sequence of 
characters. Characters will be one of the following: P, representing an airport square; 1,...,9, 
representing a wind velocity in a square without an airplane; A,B, ...,I represent a square 
containing an airplane with a wind velocity between 1 and 9; J represents a square containing 
an airplane at an airport. Lines are distinguished from each other by a single newline 
character (not CRLF). At most one square of the map will have an airplane, all other squares 
have wind velocities or airports. The weather never changes on our maps, nor do the locations 
of the airports. The goal of your program will be to output a sequence of maps which take the 
initial location of an airplane to an airport. Between maps the airplane can move at most one 
square at a time up, down, left, or right. If an airplane is on a square with wind 
velocity x, it take x units of fuel to leave that square. If an airplane uses all of its fuel 
it can no longer move. As an example, a file weather.txt might contain the following:

B317
53P7

To run plane_agent.py, I might type:

python plane_agent.py weather.txt euclidean 7
There is a way for a plane with a fuel of 7 to find an airport. So on this input the program outputs a sequence of maps and fuel statuses such as:

Map:1 Fuel:7
B317
53P7
Map:2 Fuel:5
2C17
53P7
Map:3 Fuel:2
23A7
53P7
Map:4 Fuel:1 Found an Airport!
2317
53J7
The file containing a map might contain, in general, a map of size much bigger than 2x4. Maps might also contain more than one airport. It is also quite possible that there is no path that takes an airplane to an airport without running out of fuel. In this case, your program should just output:

No route exists.
To find a sequence of maps, your code should use an implementation of the A⋆ algorithm. As a heuristic, it should use the command line parameter to decide to use either manhattan distance (ignore wind velocities in computing this), euclidean distance, or a heuristic you make up. You should have at the top of your program have comments saying where to find the A⋆ code and heuristics.

The teams with the best made_up function on the sequence of tests used for your homework will receive 1 bonus point. That completes the description the homework. Good Luck!
test edit
dkkasd
git this
hello 