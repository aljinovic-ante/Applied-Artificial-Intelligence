from State import State

def solution_bfs(game):
    queue = [(game, [])]
    visited = set()
    cnt=0
    
    while queue:
        state, path = queue.pop(0)
        if state.is_solved():
            full_path = path+ [state]
            break
        
        visited.add(state.string)
        if state.is_terminal():
            state.undo_action()
            continue
        
        for next_state in state.next_states():
            cnt+=1
            if next_state.string not in visited:
                queue.append((next_state, path + [state]))
    
    for part in full_path:
        print("part: ", part.__str__())
    
    print("len: ", len(full_path))
    print("cnt: ", cnt)

game = State()
solution_bfs(game)