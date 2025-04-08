from State import State

def heuristic(state):
    right_side = state.string.split(" || ")[1]
    sum = 0
    for letter in "VOK":
        if letter in right_side:
            sum += 1
    return sum

def bestFS(game):
    queue = [(heuristic(game), game, [])]
    visited = set()
    
    while queue:
        queue.sort(key=lambda x: x[0], reverse=True)
        h, state, path = queue.pop(0)
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
            left, right = next_state.string.split(" || ")
            sorted_next_state = ''.join(sorted(left)) + " || " + ''.join(sorted(right))
            if sorted_next_state not in visited:
                queue.append((heuristic(next_state), next_state, path + [state]))
    
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
bestFS(game)
