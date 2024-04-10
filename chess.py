from searching_framework import *
class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial,goal)

    def check_stars(self, figure, stars):
        stars_list = [(x,y) for (x,y) in stars]
        if figure in stars_list:
            stars_list.remove(figure)

        return tuple(stars_list)
    
    def move_figure(self, f1, move_coords, f2):
        #to check if f1 != f2
        new_x, new_y = f1[0] + move_coords[0] , f1[1] + move_coords[1]

        if 0 <= new_x <= 7 and 0 <= new_y <= 7 and (new_x, new_y) != f2:
            return (new_x, new_y)
        return None

    def successor(self, state):
        successors = dict()
        horse, bishop, stars = state

        horse_actions=["K1","K2","K3","K4","K5","K6","K7","K8"]
        bishop_actions=["B1","B2","B3","B4"]

        horse_moves = [(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,2)]
        bishop_moves = [(-1,1),(1,1),(-1,-1),(1,-1)]

        #MOVE HORSE
        for action, move in zip(horse_actions, horse_moves):
            new_horse = self.move_figure(horse, move, bishop)
            if new_horse is not None:
                new_stars = self.check_stars(new_horse, stars)
                successors[action] = (new_horse, bishop, new_stars)

        for action, move in zip(bishop_actions, bishop_moves):
            new_bishop = self.move_figure(bishop, move, horse)
            if new_bishop is not None:
                new_stars = self.check_stars(new_bishop, stars)
                successors[action] = (horse, new_bishop, new_stars)

        return successors

    def actions(self, state):
            return self.successor(state).keys()

    def result(self, state, action):
            return self.successor(state)[action]

    def goal_test(self, state):
            return len(state[-1]) == 0

if __name__ == '__main__':
    input_horse = input().split(',')
    input_bishop = input().split(',')
    horse = (int(input_horse[0]), int(input_horse[1]))
    bishop = (int(input_bishop[0]), int(input_bishop[1]))

    stars = ((1,1),(4,3),(6,6))

    problem = Stars((horse, bishop, stars))
    solution = breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
