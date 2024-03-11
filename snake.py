from utils import *
from uninformed_search import *
class Snake(Problem):
    def __init__(self, r_apples, initial, goal=None):
        super().__init__(initial, goal)
        self.r_apples = r_apples

    def move_head(self, x1, y1, x2, y2, snake_body, direction):
        x1 += x2
        y1 += y2
        if 0 <= x1 <= 9 and 0 <= y1 <= 9 and (x1, y1) not in self.r_apples and (x1, y1) not in snake_body:
            return (x1, y1, direction)
        else:
            return None

    def update_green_apples(self, x, y, green_apples):
        green_apples = list(green_apples)
        if (x, y) in green_apples:
            green_apples.remove((x,y))
            return green_apples

        return None

    def successor(self, state):
        successors = dict()

        directions = {"A": (1, 0), "B": (-1, 0), "C": (0, -1), "D": (0, 1)}

        snake, green_apples = list(state)
        snake_head = snake[0]
        snake_body = snake[1::]

        # ProdolzhiPravo
        new_head = self.move_head(snake_head[0], snake_head[1], directions[snake_head[2]][0],
                                  directions[snake_head[2]][1],
                                  snake_body, snake_head[2])

        if new_head is not None:
            tmp_last_body_part = snake[-1]
            new_snake = [(snake[i - 1][0],snake[i-1][1]) if i==1 else snake[i-1] for i in range(len(snake))]
            new_snake[0] = new_head
            new_apples = self.update_green_apples(new_head[0], new_head[1], green_apples)
            if new_apples is not None:
                new_snake.append(tmp_last_body_part)
            else:
                new_apples = green_apples

            successors["ProdolzhiPravo"] = (tuple(new_snake), tuple(new_apples))

        # SvrtiDesno
        if snake_head[2] == "A":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["C"][0], directions["C"][1], snake_body,
                                      "C")
        elif snake_head[2] == "B":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["D"][0], directions["D"][1], snake_body,
                                      "D")
        elif snake_head[2] == "C":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["B"][0], directions["B"][1], snake_body,
                                      "B")
        elif snake_head[2] == "D":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["A"][0], directions["A"][1], snake_body,
                                      "A")

        if new_head is not None:
            tmp_last_body_part = snake[-1]
            new_snake = [(snake[i - 1][0],snake[i-1][1]) if i==1 else snake[i-1] for i in range(len(snake))]
            new_snake[0] = new_head
            new_apples = self.update_green_apples(new_head[0], new_head[1], green_apples)
            if new_apples is not None:
                new_snake.append(tmp_last_body_part)
            else:
                new_apples = green_apples

            successors["SvrtiDesno"] = (tuple(new_snake), tuple(new_apples))

        # SvrtiLevo
        if snake_head[2] == "A":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["D"][0], directions["D"][1], snake_body,
                                      "D")
        elif snake_head[2] == "B":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["C"][0], directions["C"][1], snake_body,
                                      "C")
        elif snake_head[2] == "C":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["A"][0], directions["A"][1], snake_body,
                                      "A")
        elif snake_head[2] == "D":
            new_head = self.move_head(snake_head[0], snake_head[1], directions["B"][0], directions["B"][1], snake_body,
                                      "B")

        if new_head is not None:
            tmp_last_body_part = snake[-1]
            new_snake = [(snake[i - 1][0],snake[i-1][1]) if i==1 else snake[i-1] for i in range(len(snake))]
            new_snake[0] = new_head
            new_apples = self.update_green_apples(new_head[0], new_head[1], green_apples)
            if new_apples is not None:
                new_snake.append(tmp_last_body_part)
            else:
                new_apples = green_apples

            successors["SvrtiLevo"] = (tuple(new_snake), tuple(new_apples))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

if __name__ == "__main__":
    snake = [(0, 7, "C"), (0, 8), (0, 9)]
    n = int(input())
    gr_apples = []
    for i in range(n):
        coordinates = input().split(",")
        coordinates = tuple(map(int, coordinates))
        gr_apples.append(tuple(coordinates))

    red_apples = []
    n = int(input())
    for i in range(n):
        coordinates = input().split(",")
        coordinates = tuple(map(int, coordinates))
        red_apples.append(tuple(coordinates))

    snake_problem = Snake(red_apples, (tuple(snake), tuple(gr_apples)), None)

    snake_problem_solution = breadth_first_graph_search(snake_problem)
    if snake_problem_solution is not None:
        print(snake_problem_solution.solution())
