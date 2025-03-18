from State import State

def heuristic(state):
    right_side = state.string.split(" || ")[1]
    sum=0
    for letter in "VOK":
        if letter in right_side:
            sum+=1
            
    return sum

def bestFS(game):
    queue = [(heuristic(game), game, [])]
    visited = set()
    
    while queue:
        queue.sort(key=lambda x: x[0], reverse=True)
        h, state, path = queue.pop(0)
        
        if state.is_solved():
            full_path = path + [state]
            break
        
        visited.add(state.string)
        
        if state.is_terminal():
            state.undo_action()
            continue
        
        for next_state in state.next_states():
            if next_state.string not in visited:
                queue.append((heuristic(next_state), next_state, path + [state]))
    
    for part in full_path:
        print("part: ", part.__str__())
    
    print("len: ", len(full_path))

game = State()
bestFS(game)
