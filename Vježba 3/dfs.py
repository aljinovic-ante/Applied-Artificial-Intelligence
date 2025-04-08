from State import State

def solution_dfs(game):
    stack = [(game, [])]
    visited = set()
    cnt = 0
    
    while stack:
        state, path = stack.pop()
        left, right = state.string.split(" || ")
        sorted_string = ''.join(sorted(left)) + " || " + ''.join(sorted(right))

        if sorted_string in visited:
            continue
        
        if state.is_solved():
            full_path = path + [state]
            break
        
        visited.add(sorted_string)
        
        if state.is_terminal():
            state.undo_action()
            continue
        
        for next_state in state.next_states():
            cnt += 1
            left, right = next_state.string.split(" || ")
            sorted_next_state = ''.join(sorted(left)) + " || " + ''.join(sorted(right))
            if sorted_next_state not in visited:
                stack.append((next_state, path + [state]))
    
    cnt2 = 0
    for part in full_path:
        print("STEP: ", cnt2)
        print("part: ", part.__str__())
        cnt2 += 1
    
    print("len: ", len(visited))
    cnt3=0
    for vis in visited:
        cnt3+=1
        print(vis)
    print("cnt3: ", cnt3)

game = State()
solution_dfs(game)
