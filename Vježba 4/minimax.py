from dots_and_boxes import State


class MinimaxAgent:

    VALUES = [ 0, 100, -100, 0 ]
    
    def __init__(self, maxdepth=4):
        self.maxdepth = maxdepth
        self.nodes = 0
        self.transposition_table = {}

    def score(self, state):
        return len(state.boxes[0]) - len(state.boxes[1])

    def sorted_actions(self, state):
        actions = state.all_actions()
        key = str(state)
        best_action = None
        if key in self.transposition_table:
            best_action = self.transposition_table[key][0]
        scored_actions = []
        for action in actions:
            from_point = action[0]
            to_point = action[1]
            num_boxes = len(state.closed_boxes(from_point[0], from_point[1], to_point[0], to_point[1]))
            scored_actions.append((num_boxes, action))
        scored_actions.sort(reverse=True)
        sorted_list = []
        for score, action in scored_actions:
            sorted_list.append(action)
        if best_action and best_action in sorted_list:
            sorted_list.remove(best_action)
            sorted_list.insert(0, best_action)
        return sorted_list

    def minimax(self, state, alpha, beta, depth):
        self.nodes += 1
        key = str(state)
        if key in self.transposition_table:
            saved_action, saved_value, saved_depth, exact = self.transposition_table[key]
            if exact and saved_depth >= depth:
                return saved_action, saved_value

        if state.terminal() != State.ONGOING:
            return None, self.VALUES[state.terminal()]

        if depth == 0:
            return None, self.score(state)

        best = None
        exact = True

        if state.turn == 0:
            for action in self.sorted_actions(state):
                state.action(action)
                _, value = self.minimax(state, alpha, beta, depth - 1)
                state.undo(action)
                if value > alpha:
                    alpha = value
                    best = action
                if alpha >= beta:
                    exact = False
                    break
            value = alpha
        else:
            for action in self.sorted_actions(state):
                state.action(action)
                _, value = self.minimax(state, alpha, beta, depth-1)
                state.undo(action)
                if value < beta:
                    beta = value
                    best = action
                if alpha >= beta:
                    exact = False
                    break
            value = beta

        self.transposition_table[key] = (best, value, depth, exact)
        return best, value

    def action(self, state: State):
        self.nodes = 0
        return self.minimax(state, -1000, 1000, self.maxdepth)    

if __name__ == "__main__":
    game = State(5)
    agent = MinimaxAgent(6)
    while game.terminal() == State.ONGOING:
        print(game)
        action, value = agent.action(game)  
        print("action:", action, "value:", value, "nodes", agent.nodes)
        game.action(action)
    print("game over:", game.terminal())
    print(game)
    