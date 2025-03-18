from copy import deepcopy

class State:
    def __init__(self):
        self.string="VOKB || ----"
        self.in_boat=""
    
    def __str__(self):
        return self.string
    
    def all_actions(self):
        actions=[]
        left,right=self.string.split(" || ")
        print("STANJE: ", left,right)
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
        next_states_list=[]
        actions=self.all_actions()
        for action in actions:
            state=self.copy()
            state.action(action)
            next_states_list.append(state)
        for state_for in next_states_list:
            print("stanje: ",state_for.__str__())
        return next_states_list

    def action(self, act):
        left, right = self.string.split(" || ")
        print("ACT in action: ",act)
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
        print("posli action: ",self.__str__())
                
    def undo_action(self):
        pass

    def copy(self):
        return deepcopy(self)

    def is_solved(self):
        return self.string[:4]=="----"
    
    def is_terminal(self):
        left,right=self.string.split(" || ")
        sorted(left)
        sorted(right)

        if(right=="BKOV"):
            return True
        
        terminal_states=["OV","KO"]

        for t_state in terminal_states:
            if t_state in left and "B" not in left:
                return True
            if t_state in right and "B" not in right:
                return True
        
        return False


game=State()
print("POCETNO ",game.__str__())
i=0
while True:
    print("i ",i)
    nxt_st=game.next_states()
    for nxt_s in nxt_st:
        print("nxt st ",nxt_s.__str__())
    i+=1
    print("i ",i)
    if i>3:
        break
        
