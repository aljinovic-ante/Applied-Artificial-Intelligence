from copy import deepcopy

class State:
    def __init__(self):
        self.string="VOKB || ----"
        self.in_boat=""
        self.history = []
    
    def __str__(self):
        return self.string + " In Boat: " + self.in_boat
    
    def all_actions(self):
        actions=[]
        left,right=self.string.split(" || ")
        #print("STANJE: ", left,right)
        if "B" in left:
            actions.append("SAIL")
            if self.in_boat=="":
                for letter in left:
                    if letter!="-" and letter!="B":
                        actions.append("BOARD "+letter)
            else:
                actions.append("DISEMBARK "+self.in_boat)
                
        elif "B" in right:
            actions.append("SAIL")
            if self.in_boat=="":
                for letter in right:
                    if letter!="-" and letter!="B":
                        actions.append("BOARD "+letter)
            else:
                actions.append("DISEMBARK "+self.in_boat)
                
        return actions

    def next_states(self):
        states = []
        actions=self.all_actions()
        for action in actions:
            state = self.copy()
            state.action(action)
            states.append(state)
        return states

    def action(self, act):
        self.history.append((self.string, self.in_boat))
        left, right = self.string.split(" || ")
        #print("ACT in action: ",act)
        parts = act.split(" ")
        if len(parts) == 2:
            act, letter = parts
        else:
            act, letter = parts[0], None

        if "B" in left:
            if act == "SAIL":
                left = left.replace("B", "-", 1)
                right = right.replace("-", "B", 1)
            elif act == "BOARD" and letter in left:
                left = left.replace(letter, "-", 1)
                self.in_boat = letter
            elif act == "DISEMBARK" and letter == self.in_boat:
                left = left.replace("-", letter, 1)
                self.in_boat = ""

        elif "B" in right:
            if act == "SAIL":
                right = right.replace("B", "-", 1)
                left = left.replace("-", "B", 1)
            elif act == "BOARD" and letter in right:
                right = right.replace(letter, "-", 1)
                self.in_boat = letter
            elif act == "DISEMBARK" and letter == self.in_boat:
                right = right.replace("-", letter, 1)
                self.in_boat = ""

        self.string= left + " || " + right
                
    def undo_action(self):
        if self.history:
            self.string, self.in_boat = self.history.pop()

    def copy(self):
        return deepcopy(self)

    def is_solved(self):
        right_side = self.string.split(" || ")[1]
        return self.string[:4] == "----" and "B" in right_side and "K" in right_side and "O" in right_side and "V" in right_side
    
    def is_terminal(self):
        left, right = self.string.split(" || ")
        
        if "O" in left and "V" in left and "B" not in left:
            return True
        if "O" in right and "V" in right and "B" not in right:
            return True
        
        if "O" in left and "K" in left and "B" not in left:
            return True
        if "O" in right and "K" in right and "B" not in right:
            return True

        return False


