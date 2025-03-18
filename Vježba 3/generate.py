from State import State

def generate(game, visited):
    if game.string in visited:
        return
    visited[game.string] = game.copy()
    for action in game.all_actions():
        game.action(action)
        print("STANJE:", game.__str__())
        generate(game, visited)
        game.undo_action()
    
graph = {}
game=State()
generate(game, graph)
for key,value in sorted(graph.items()):
    print(key)

        