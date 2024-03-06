#tocna e samo mi se poinaku po red krsteni kaj konjot 
from utils import *
from uninformed_search import *
class Chess(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        # GRID SIZE 8X8

    def move_horse(self, horse, coordinates):
        horse_x = horse[0] + coordinates[0]
        horse_y = horse[1] + coordinates[1]

        if 0 <= horse_x <= 7 and 0 <= horse_y <= 7:
            return horse_x, horse_y
        else:
            return None

    def move_lovec(self, lovec, coordinates):
        lovec_x = lovec[0] + coordinates[0]
        lovec_y = lovec[1] + coordinates[1]

        if 0 <= lovec_x <= 7 and 0 <= lovec_y <= 7:
            return lovec_x, lovec_y
        else:
            return None

    def successor(self, state):
        successors = dict()

        horse, lovec, stars = state

        horse_directions = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"]
        horse_new_coordinates = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1), (-1, -2), (1, -2)]

        for direction, coordinates in zip(horse_directions, horse_new_coordinates):
            new_horse = self.move_horse(horse, coordinates)

            if new_horse is not None and new_horse != lovec:
                if new_horse in stars:
                    new_stars = list(stars)
                    new_stars.remove(new_horse)
                    successors[direction] = (new_horse, lovec, tuple(new_stars))
                else:
                    successors[direction] = (new_horse, lovec, stars)

        lovec_directions = ["B1", "B2", "B3", "B4"]
        lovec_new_coordinates = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

        for direction, coordinates in zip(lovec_directions, lovec_new_coordinates):
            new_lovec = self.move_lovec(lovec, coordinates)

            if new_lovec is not None and new_lovec != horse:
                if new_lovec in stars:
                    new_stars = list(stars)
                    new_stars.remove(new_lovec)
                    successors[direction] = (horse, new_lovec, tuple(new_stars))
                else:
                    successors[direction] = (horse, new_lovec, stars)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


horse = (2, 5)
lovec = (5, 1)
stars = ((1, 1), (4, 3), (6, 6))
problem = Chess((horse, lovec, stars), None)

p_solution = breadth_first_graph_search(problem)
if p_solution is not None:
    print(p_solution.solution())
