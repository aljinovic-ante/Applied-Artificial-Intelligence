from State import State

def solution_dfs(game):
    stack = [(game, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        if state.is_solved():
            full_path = path+ [state]
            break
        
        visited.add(state.string)
        if state.is_terminal():
            state.undo_action()
            continue
        
        for next_state in state.next_states():
            if next_state.string not in visited:
                stack.append((next_state, path + [state]))
    
    for part in full_path:
        print("part: ", part.__str__())
    
    print("len: ", len(full_path))
    

game=State()
solution_dfs(game)
