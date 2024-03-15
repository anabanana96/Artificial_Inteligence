class Football(Problem):
    def __init__(self, opponents, initial, goal=None):
        super().__init__(initial,goal)
        self.opponents = opponents

    def move_player(self, current_position, move_direction, ball_position):
        new_x = current_position[0] + move_direction[0]
        new_y = current_position[1] + move_direction[1]
    
        if 0 <= new_x <= 7 and 0 <= new_y <= 5 and (new_x, new_y) not in self.opponents and (new_x, new_y) != ball_position:
            return (new_x, new_y)
        else:
            return None

    def move_ball(self, x1, y1, x2, y2):
        x1+=x2
        y1+=y2
        if (x1,y1) in self.opponents or x1 <0 or x1 > 7 or y1 < 0 or y1 > 5:
            return None

        for x in range(0,2):
            for y in range(-1,2):
                if (x,y)!=(0,0) and (x1+x,y1+y) in self.opponents:
                    return None

        return (x1,y1)
        
    def check_ball_in_front(self, player_position, move_direction, ball_position):
        new_player_position = (player_position[0] + move_direction[0], player_position[1] + move_direction[1])
        return new_player_position == ball_position

    def successor(self, state):
        actions = {}

        player, ball = state

        player_direction = {(0,1): "Pomesti coveche gore", (0,-1):"Pomesti coveche dolu", (1,0):"Pomesti coveche desno",
                            (1,1):"Pomesti coveche gore-desno", (1,-1):"Pomesti coveche dolu-desno"}

        ball_direction = {(0,1):"Turni topka gore", (0,-1):"Turni topka dolu",(1,0):"Turni topka desno",
                          (1,1):"Turni topka gore-desno", (1,-1):"Turni topka dolu-desno"}

        for coordinates in player_direction.keys():
            if self.check_ball_in_front(player, coordinates, ball) == True:
                ball_new = self.move_ball(ball[0],ball[1],coordinates[0],coordinates[1])
                pl_new = self.move_player(player, coordinates, ball_new)
                if ball_new is not None and pl_new is not None:
                    action = ball_direction[coordinates]
                    actions[action] = (pl_new, ball_new)
            else:
                pl_new = self.move_player(player, coordinates, ball)
                if pl_new is not None:
                    action = player_direction[coordinates]
                    actions[action] = (pl_new, ball)

        return actions

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal

if __name__ == "__main__":
    player_position = tuple(map(int, input().split(",")))
    ball_position = tuple(map(int, input().split(",")))
    opponents = [(3, 3), (5, 4)]
    goals = ((7, 2), (7, 3))
    football_problem = Football(opponents, (player_position, ball_position), goals)
    solution = breadth_first_graph_search(football_problem)
    if solution is not None:
        print(solution.solution())
