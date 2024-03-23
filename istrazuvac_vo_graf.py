from utils import *
from uninformed_search import *
class Explorer(Problem):
    def __init__(self, possible_starts, initial, goal=None):
        super().__init__(initial, goal)
        self.possible_starts = possible_starts

    def move_player(self, player, coords, p_edges):
        if player != ():
            new_x = player[0] + coords[0]
            new_y = player[1] + coords[1]

            if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_x, new_y) not in p_edges and (new_y, new_x) not in p_edges:
                return (new_x, new_y)

        return None

    def successor(self, state):
        successors = dict()
        player, p_edges, stars = state
        directions = ["up", "down", "left", "right"]
        coordinates = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        new_edges = [x for x in p_edges]

        if player == ():
            for start in self.possible_starts:
                successors[f"Igrachot zapocnuva na {start}"] = (start, p_edges, stars)

        if player == (1, 2):
            directions.extend(["down-right"])
            coordinates.extend([(1, -1)])
        elif player == (2, 1):
            directions.extend(["up-left"])
            coordinates.extend([(-1, 1)])

        for direction, coords in zip(directions, coordinates):
            new_player = self.move_player(player, coords, p_edges)
            if new_player is not None:
                if new_player in stars:
                    stars = tuple(block for block in stars if block != new_player)

                new_edge = (player, new_player) if player < new_player else (new_player, player)
                if new_edge not in new_edges:
                    new_edges.append(new_edge)
                    successors[direction] = (new_player, tuple(new_edges), stars)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


possible_starts = ((1,1),(2,1),(2,2),(1,2))
prohibit_edges = (((0,1),(0,2)) , ((1,0),(2,0)) , ((3,1),(3,2)) , ((1,3),(2,3))) #zabraneti rebra za dvizenje
#ke ima uslov samo ako se naogja na poz (1,2) ili (2,1) deka moze da se pridvizi dole-desno ako e na (1,2) ili gore-levo ako se naogja na (2,1)
stars = ((0,3),(3,0))
explorer = Explorer(possible_starts, ((), prohibit_edges, stars), goal=None)
explorer_solution = breadth_first_graph_search(explorer)
if explorer_solution is not None:
    print(explorer_solution.solution())
