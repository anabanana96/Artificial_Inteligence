from utils import *
from uninformed_search import *

class Molecules(Problem):
    def __init__(self, obstacles, init, goal=None):
        super().__init__(init,goal)
        self.obstacles = obstacles

    def move_right(self, x1, y1, x2, y2, x3, y3):
        while x1+1 < 9 and (x1+1, y1) not in self.obstacles and (x1 + 1, y1)!=(x2,y2) and (x1+1, y1)!=(x3,y3):
            x1 += 1

        return x1

    def move_left(self, x1, y1, x2, y2, x3, y3):
        while x1 - 1 >= 0 and (x1 - 1, y1) not in self.obstacles and (x1 - 1, y1) != (x2, y2) and (x1 - 1, y1) != (x3, y3):
            x1 -= 1

        return x1

    def move_up(self, x1, y1, x2, y2, x3, y3):
        while y1 + 1 < 7 and (x1, y1+1) not in self.obstacles and (x1, y1+1)!=(x2,y2) and (x1,y1+1)!=(x3,y3):
            y1 += 1

        return y1

    def move_down(self, x1, y1, y2, x2, x3, y3):
        while y1 - 1 >= 0 and (x1, y1 - 1) not in self.obstacles and (x1, y1 - 1) != (x2, y2) and (x1, y1 - 1) != (x3, y3):
            y1 -= 1

        return y1

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]

        #MOVE H1
        right_h1 = self.move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y)
        successors["RIGHT_H1"] = (right_h1, h1_y, o_x, o_y, h2_x, h2_y)
        left_h1 = self.move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y)
        successors["LEFT_H1"] = (left_h1, h1_y, o_x, o_y, h2_x, h2_y)
        up_h1 = self.move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y)
        successors["UP_H1"] = (h1_x, up_h1, o_x, o_y, h2_x, h2_y)
        down_h1 = self.move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y)
        successors["DOWN_H1"] = (h1_x, down_h1, o_x, o_y, h2_x, h2_y)

        #MOVE OXYGEN
        right_o = self.move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        successors["RIGHT_O"] = (right_o, o_y, h1_x, h1_y, h2_x, h2_y)
        left_o = self.move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        successors["LEFT_O"] = (left_o, o_y, h1_x, h1_y, h2_x, h2_y)
        up_o = self.move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        successors["UP_O"] = (o_x, up_o, h1_x, h1_y, h2_x, h2_y)
        down_o = self.move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        successors["DOWN_O"] = (o_x, down_o, h1_x, h1_y, h2_x, h2_y)

        #MOVE H2
        right_h2 = self.move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y)
        successors["RIGHT_H2"] = (right_h2, h2_y, o_x, o_y, h1_x, h1_y)
        left_h2 = self.move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y)
        successors["LEFT_H2"] = (left_h2, h2_y, o_x, o_y, h1_x, h1_y)
        up_h2 = self.move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y)
        successors["UP_H2"] = (h2_x, up_h2, o_x, o_y, h1_x, h1_y)
        down_h2 = self.move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y)
        successors["DOWN_H2"] = (h2_x, down_h2, o_x, o_y, h1_x, h1_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]

        return (h1_x, h1_y) == (o_x - 1, o_y) and (h2_x, h2_y) == (o_x + 1, o_y)


h1 = (2,1)
h2 = (2,6)
oxygen = (7,2)

obstacles = ((0,1),(1,1),(3,1),(6,1),(4,2),(6,2),(1,3),(6,3),(7,3),(2,5),(8,5),(3,6),(5,6),(7,6))

problem = Molecules(obstacles, (h1[0], h1[1], oxygen[0], oxygen[1], h2[0], h2[1]), None)
p_solution = breadth_first_graph_search(problem)

if p_solution is not None:
    print(p_solution.solution())
