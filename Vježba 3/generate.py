from State import State

def generate():
    graph = {}
    
    def rec(state):
        left, right = state.string.split(" || ")
        sorted_string = ''.join(sorted(left)) + " || " + ''.join(sorted(right))
        
        if sorted_string in graph:
            return
        
        graph[sorted_string] = state
        
        if state.is_terminal() or state.is_solved():
            return
        
        for next_state in state.next_states():
            rec(next_state)
    
    rec(State())
    return graph

cnt = 0
for state in generate().values():
    print(state)
    cnt += 1
print("cnt: ", cnt)
