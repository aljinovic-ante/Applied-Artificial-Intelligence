
from dots_and_boxes import State


class MinimaxAgent:

    VALUES = [ 0, 100, -100, 0 ]
    
    def __init__(self, maxdepth=4):
        self.maxdepth = maxdepth
        self.nodes = 0
    
    def score(self, state):
        return 0
    
    def sorted_actions(self, state):
        return state.all_actions()
    
    def minimax(self, state, alpha, beta, depth):
        self.nodes += 1
        if state.terminal() != State.ONGOING:
            return None, self.VALUES[state.terminal()]
        if depth == 0:
            return None, self.score(state)
        best = None
        if state.turn == 0:
            for action in self.sorted_actions(state):
                state.action(action)
                _, value = self.minimax(state, alpha, beta, depth-1)
                state.undo(action)
                if value > alpha:
                    alpha = value
                    best = action
                if alpha >= beta:
                    break
            return best, alpha
        else:
            for action in self.sorted_actions(state):
                state.action(action)
                _, value = self.minimax(state, alpha, beta, depth-1)
                state.undo(action)
                if value < beta:
                    beta = value
                    best = action
                if alpha >= beta:
                    break
            return best, beta

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
        