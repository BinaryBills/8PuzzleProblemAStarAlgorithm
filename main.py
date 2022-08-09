#Author: BinaryBills
#Creation Date: July 5, 2022
#Date Modified: July 23, 2022
#Purpose: Using the A* search algorithm, this program provides instructions for
#a problem-solving AI agent to find the optimal solution for an eight puzzle 
#problem. As preface information to understand the game, the objective of 
#a sliding eight puzzle is to slide the tiles horizontally or vertically 
#into the empty space on the 3x3 grid until the configuration matches 
#the specified goal. Lastly, this program is based on Tristian 
#Penman's N-Puzzle solver and should produce the same results.
import Puzzle, Node
import os
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

############################################
#        Setting the initial and           #
#             the goal state               #
############################################
def setStates(initSt = [1,5,"-",6,7,4,2,8,3], goalSt = [7,6,5,8,"-",4,1,2,3] ):
     return Puzzle.puzzleSt(initSt,goalSt)

############################################
#          Creates Dataclass to            #
#        set priority for frontier         #
#                 Nodes                    #
############################################
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

############################################
#        Hashes Node in explored set       #
############################################
def addToHT(d, node):
   if d.get(hash(node)) == None:
       d[hash(node)] = node
   else:
        pass
  
############################################
#        A* Search Algorithm               #
#        using Manhattan Distance          #
############################################
def A_Star(r):
    frontier = PriorityQueue()
    explored = {}
    frontier.put(PrioritizedItem(r.f, r))
    count = 1

    while(frontier.empty() == False):
        temp = frontier.get().item
        print("------------------------------------------")
        print("Expansion",count,":")
        
        temp.display
        addToHT(explored,temp)

        if temp.isGoal == True:
            print("Goal found! Thank you for using my program!")
            break

        print("Possible Moves from Current State:")
        children = temp.expand

        for n in children:
           print(n.action)
           print(n.displayChild)
           frontier.put(PrioritizedItem(n.f, n))
        os.system("PAUSE")
        count+=1


############################################
#                  Main                    #
#                Execution                 #
############################################
def main():
    #Creates a root node initialized to values specified in setStates()
    #If you want to change initSt and goalSt values, pass it into the setStates() function.
    r = Node.Node(setStates())
    A_Star(r)
main()
