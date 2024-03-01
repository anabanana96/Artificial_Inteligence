from utils import *
from uninformed_search import *

class Explorer(Problem):
    def __init__(self, obstacle1, obstacle2, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacle1 = list(obstacle1)
        self.obstacle2 = list(obstacle2)
        self.gridSize = [8,6]

    def move_obstacle(self, obstacle):
        if obstacle[2] == 1: #if it moves up
            if obstacle[1] == self.gridSize[1] - 1: #if it has reached the top
                obstacle[2] = -1
                obstacle[1] -= 1
            else:
                obstacle[1] += 1
        else:
            if(obstacle[1]==0):
                obstacle[2] = 1
                obstacle[1] += 1
            else:
                obstacle[1] -= 1

    def successor(self, state):
        obstacles = [(obstacle1[0],obstacle1[1]), (obstacle2[0],obstacle2[1])]

        self.move_obstacle(self.obstacle1)
        self.move_obstacle(self.obstacle2)

        man_x = state[0]
        man_y = state[1]

        successors = {}

        #MOVE RIGHT
        if man_x + 1 < self.gridSize[0] and (man_x + 1, man_y) not in obstacles:
            successors["right"] = (man_x + 1, man_y)
        if man_x - 1 <= 0 and (man_x - 1, man_y) not in obstacles:
            successors["left"] = (man_x - 1, man_y)
        if man_y + 1 < self.gridSize[1] and (man_x, man_y + 1) not in obstacles:
            successors["up"] = (man_x, man_y + 1)
        if man_y - 1 <= 0 and (man_x, man_y - 1) not in obstacles:
            successors["down"] = (man_x, man_y - 1)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == "__main__":
    goalState = (7,4)
    startState = (0,2)
    obstacle1 = (2,5,-1) #-1 going down
    obstacle2 = (5,0,1) #1 going up

    explorer = Explorer(obstacle1, obstacle2, startState, goalState)
    print(breadth_first_graph_search(explorer).solution())
