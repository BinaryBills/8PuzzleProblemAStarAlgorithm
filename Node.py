
class Node(object):
    """
    A class that represents a state space search tree node.
    -> 'St' is an instance of puzzleSt
    -> 'parent' is the parent state 
    -> 'action' is the move used to produce the state
    -> 'g' refers to the g(n)
    -> 's' is used to keep track of number of moves the algorithm made
    """
    def __init__(self,state, parent = None, action = None):
        self.st = state
        self.parent = parent
        self.action = action
        if (self.parent):
            self.g = parent.g + self.pathCost
            self.s = parent.s + 1
        else:
            self.g = 0
            self.s = 1

    @property
    def expand(self):
        """
        Returns list of child nodes
        """
        children = []
        moves = self.Action
        for option in moves:
             children.append(self.get_result(option))
        return children


    @property
    def pathCost(self):
        """
        Returns cost associated with performing an action.
        Modify these values if you want to change the cost.
        """
        if (self.action == 'West' or self.action == 'East'):
            return 1
        elif (self.action == 'North'):
            return 1
        elif (self.action == 'South'):
            return 1
        else:
            return 0

    @property
    def f(self):
        """
        The Heuristic evaluation function
        Calculation of f(n) = g(n) + h(n)
        """
        return (self.g + self.st.h)

    @property
    def Action(self):
        """
        Wrapper for Actions in current state.
        Returns list of possible actions.
        """
        return self.st.Action

    @property
    def display(self):
        """
        Wrapper for the display function.
        """
        self.st.display(self.g,self.action,self.f,self.s)

    @property
    def displayChild(self):
        """
        Wrapper for the display function.
        """
        return self.st.get_Table()

    @property
    def isGoal(self):
        """
        Checks if goal has been found
        """
        return self.st.st == self.st.goalSt

    def get_result(self,a):
        """
        Wrapper for Results in current state.
        Creates a new node with state
        """
        return Node(self.st.Result(a),self,a)

    