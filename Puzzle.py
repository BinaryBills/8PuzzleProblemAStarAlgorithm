from tabulate import tabulate

class puzzleSt(object):
    """
    A class that represents an individual state 
    for a sliding 8 puzzle.
    """
    def __init__(self,initialState,goalState):
        self.st = initialState
        self.goalSt = goalState
        self.cost = 0

    @property
    def isGoal(self):
     """
     Algoritm completed if current state
     is the same as the goal state
     """
     return (self.St == self.goalSt)

    @property
    def Action(self):
     """
     Returns a list of moves that the blank tile
     on the grid can currently execute.
     """
     moves = ['West','East','South','North']
     empTileIndex = self.st.index("-")

     if empTileIndex % 3 == 0:
        moves.remove('West')

     if empTileIndex % 3 == 2:
         moves.remove('East')
    
     if empTileIndex < 3:
        moves.remove('South')

     if empTileIndex > 5:
        moves.remove('North')
     return moves    

    @property
    def h(self):
     """
     Returns total Manhattan 
     Distance for a state.
     """
     dist = 0
     for item in self.st:
       if item != "-":
         p1 = self.XYPoint(self.st,item)
         p2 = self.XYPoint(self.goalSt,item)
         dist += self.XYDist(p1,p2)
     return dist


    def Result(self,a):
        '''
        Returns a new state that shows a 'what if'
        for executing an action
        '''
        s = puzzleSt(self.st[:],self.goalSt[:])
        empTileIndex = s.st.index("-")
        if (a == 'West'):
            s.st[empTileIndex], s.st[empTileIndex - 1] = s.st[empTileIndex - 1], s.st[empTileIndex]
        elif (a == 'North'):
             s.st[empTileIndex], s.st[empTileIndex + 3] = s.st[empTileIndex + 3], s.st[empTileIndex] 
        elif (a == 'East'):
             s.st[empTileIndex], s.st[empTileIndex + 1] = s.st[empTileIndex + 1], s.st[empTileIndex]
        elif (a == 'South'):
             s.st[empTileIndex], s.st[empTileIndex - 3] = s.st[empTileIndex - 3], s.st[empTileIndex]
        s.h
        return s
     
    
    def XYPoint(self,s,i):
     """
     Searches for the index of item i within the 1D list
     and returns what its coordinates would be if it was plotted
     on a XY graph.
     """
     
     #As reference,
     #********************************#
     #               Y+---+---+---+   #
     #          Top: 2| 1 | 5 |   |   #
     #  Initial       +---+---+---+   #
     #   State  Mid: 1| 6 | 7 | 4 |   #
     #                +---+---+---+   #
     #          Bott 0| 2 | 8 | 3 |   #
     #                +---+---+---+   #
     #               X  0   1    2    #
     #********************************#

     #********************************#
     #               Y+---+---+---+   #
     #          Top: 2| 7 | 6 | 5 |   #
     #   Goal         +---+---+---+   #
     #   State  Mid: 1| 8 |   | 4 |   #
     #                +---+---+---+   #
     #          Bott 0| 1 | 2 | 3 |   #
     #                +---+---+---+   #
     #               X  0   1    2    #
     #********************************#
     itemID = s.index(i)

     #Top Row
     if (itemID == 0):
          return [0,2]
     elif (itemID == 1):
           return [1,2]
     elif (itemID == 2):
           return [2,2]

     #Middle Row
     elif (itemID == 3):
         return [0,1]
     elif (itemID == 4):
         return [1,1]
     elif (itemID == 5):
         return [2,1]

     #Bottom Row
     if (itemID == 6):
          return [0,0]
     elif (itemID == 7):
           return [1,0]
     elif (itemID == 8):
           return [2,0]
   
    
    def XYDist(self,p1,p2):
     """
     Returns the Manhattan distance between two points
     """
     #Manhattan Distance Formula
     return( (abs(p2[0] - p1[0])   ) +   ( abs(p2[1] - p1[1])   )  )


    def get_Table(self):
         """
         Returns a table using the data from a state
         """
         s = self.st
         table_Data = [ s[0:3], s[3:6], s[6:9 ] ]
         return str(tabulate(table_Data,headers="", tablefmt = "fancy_grid", ))
   
    def display(self,c = 0,a = "None", f = 0, m = 0):
        """
        Displays a state, its path cost, heuristic, and evaluation
        """
        print("Action:", a)
        print(self.get_Table())
        result = [["g(n):",c],["h(n):",self.h],["f(n)",f]]
        print((tabulate(result,headers="", tablefmt = "fancy_grid")))
                      
                      
   



