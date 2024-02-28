import sys

class EightPuzzleGame:

    @staticmethod
    def actions(state, player):
        action_list = []
        if player == 1:
            for i in range(1, 3):
                index = state.index(str(i))
                if index == 0:
                    actions = [0, 'R', 'D']
                    if state[1] != '0':
                        actions.remove('R')
                    if state[3] != '0':
                        actions.remove('D')
                elif index == 1:
                    actions = [1, 'R', 'D', 'L']
                    if state[0] != '0':
                        actions.remove('L')
                    if state[2] != '0':
                        actions.remove('R')
                    if state[4] != '0':
                        actions.remove('D')
                elif index == 2:
                    actions = [2, 'D', 'L']
                    if state[1] != '0':
                        actions.remove('L')
                    if state[5] != '0':
                        actions.remove('D')
                elif index == 3:
                    actions = [3, 'U', 'R', 'D']
                    if state[0] != '0':
                        actions.remove('U')
                    if state[4] != '0':
                        actions.remove('R')
                    if state[6] != '0':
                        actions.remove('D')
                elif index == 4:
                    actions = [4, 'U', 'R', 'D', 'L']
                    if state[1] != '0':
                        actions.remove('U')
                    if state[3] != '0':
                        actions.remove('L')
                    if state[5] != '0':
                        actions.remove('R')
                    if state[7] != '0':
                        actions.remove('D')
                elif index == 5:
                    actions = [5, 'U', 'D', 'L']
                    if state[2] != '0':
                        actions.remove('U')
                    if state[4] != '0':
                        actions.remove('L')
                    if state[8] != '0':
                        actions.remove('D')
                elif index == 6:
                    actions = [6, 'U', 'R']
                    if state[3] != '0':
                        actions.remove('U')
                    if state[7] != '0':
                        actions.remove('R')
                elif index == 7:
                    actions = [7, 'U', 'R', 'L']
                    if state[4] != '0':
                        actions.remove('U')
                    if state[6] != '0':
                        actions.remove('L')
                    if state[8] != '0':
                        actions.remove('R')
                elif index == 8:
                    actions = [8, 'U', 'L']
                    if state[5] != '0':
                        actions.remove('U')
                    if state[7] != '0': 
                        actions.remove('L')
                if len(actions) > 1:
                    action_list.append(actions.copy())
        elif player == 2:
            for i in range(8, 10):
                index = state.index(str(i))
                if index == 0:
                    actions = [0, 'R', 'D']
                    if state[1] != '0':
                        actions.remove('R')
                    if state[3] != '0':
                        actions.remove('D')
                elif index == 1:
                    actions = [1, 'R', 'D', 'L']
                    if state[0] != '0':
                        actions.remove('L')
                    if state[2] != '0':
                        actions.remove('R')
                    if state[4] != '0':
                        actions.remove('D')
                elif index == 2:
                    actions = [2, 'D', 'L']
                    if state[1] != '0':
                        actions.remove('L')
                    if state[5] != '0':
                        actions.remove('D')
                elif index == 3:
                    actions = [3, 'U', 'R', 'D']
                    if state[0] != '0':
                        actions.remove('U')
                    if state[4] != '0':
                        actions.remove('R')
                    if state[6] != '0':
                        actions.remove('D')
                elif index == 4:
                    actions = [4, 'U', 'R', 'D', 'L']
                    if state[1] != '0':
                        actions.remove('U')
                    if state[3] != '0':
                        actions.remove('L')
                    if state[5] != '0':
                        actions.remove('R')
                    if state[7] != '0':
                        actions.remove('D')
                elif index == 5:
                    actions = [5, 'U', 'D', 'L']
                    if state[2] != '0':
                        actions.remove('U')
                    if state[4] != '0':
                        actions.remove('L')
                    if state[8] != '0':
                        actions.remove('D')
                elif index == 6:
                    actions = [6, 'U', 'R']
                    if state[3] != '0':
                        actions.remove('U')
                    if state[7] != '0':
                        actions.remove('R')
                elif index == 7:
                    actions = [7, 'U', 'R', 'L']
                    if state[4] != '0':
                        actions.remove('U')
                    if state[6] != '0':
                        actions.remove('L')
                    if state[8] != '0':
                        actions.remove('R')
                elif index == 8:
                    actions = [8, 'U', 'L']
                    if state[5] != '0':
                        actions.remove('U')
                    if state[7] != '0':
                        actions.remove('L')
                if len(actions) > 1:
                    action_list.append(actions.copy())
        return action_list

    @staticmethod
    def result(state, action, index):
        new_state = list(state)
        if action == 'U':
            new_state[index], new_state[index-3] = new_state[index-3], new_state[index]
        elif action == 'R':
            new_state[index], new_state[index+1] = new_state[index+1], new_state[index]
        elif action == 'D':
            new_state[index], new_state[index+3] = new_state[index+3], new_state[index]
        elif action == 'L':
            new_state[index], new_state[index-1] = new_state[index-1], new_state[index]
        return ''.join(new_state)
    
    @staticmethod
    def expand(node, player):
        childs = []
        action_list = EightPuzzleGame.actions(node.state, player)
        for actions in action_list:
            for action in actions[1:]:
                new_state = EightPuzzleGame.result(node.state, action, actions[0])
                child = GameNode(new_state, node, action, node.depth+1)
                childs.append(child)
        return childs
        
    

class GameNode:

    count = 0

    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def utility(self, player):
        if player == 1:
            index1 = self.state.index('1')
            index2 = self.state.index('2')
            index8 = self.state.index('8')
            index9 = self.state.index('9')
            if self.check_reverse(player):
                return -1
            if self.check_oppenent_occupienecy(player):
                return -1
            if self.check_reverse(2):
                return 1
            if self.check_oppenent_occupienecy(2):
                return 1
            if index1 + index2 == 1:
                return 1
            elif index8 + index9 == 15:
                return -1
            else:
                return 0
        elif player == 2:
            index1 = self.state.index('1')
            index2 = self.state.index('2')
            index8 = self.state.index('8')
            index9 = self.state.index('9')
            if self.check_reverse(player):
                return -1
            if self.check_oppenent_occupienecy(player):
                return -1
            if self.check_reverse(1):
                return 1
            if self.check_oppenent_occupienecy(1):
                return 1
            if index1 + index2 == 1:
                return -1
            elif index8 + index9 == 15:
                return 1
            else:
                return 0
            
    def check_reverse(self, player):
        if self.parent is None or self.parent.parent is None or self.parent.parent.parent is None or self.parent.parent.parent.parent is None: 
            return False
        if player == 1:
            index1 = self.state.index('1')
            index2 = self.state.index('2')
            grandparent = self.parent.parent
            old_index1 = grandparent.state.index('1')
            old_index2 = grandparent.state.index('2')
            very_grandparent = grandparent.parent.parent
            very_old_index1 = very_grandparent.state.index('1')
            very_old_index2 = very_grandparent.state.index('2')
            if (index1 == very_old_index1 and index1 != old_index1) or (index2 == very_old_index2 and index2 != old_index2):
                return True
            else:
                return False
        elif player == 2:
            index8 = self.state.index('8')
            index9 = self.state.index('9')
            grandparent = self.parent.parent
            old_index8 = grandparent.state.index('8')
            old_index9 = grandparent.state.index('9')
            very_grandparent = grandparent.parent.parent
            very_old_index8 = very_grandparent.state.index('8')
            very_old_index9 = very_grandparent.state.index('9')
            if (index8 == very_old_index8 and index8 != old_index8) or (index9 == very_old_index9 and index9 != old_index9):
                return True
            else:
                return False
            
    def check_oppenent_occupienecy(self, player):
        if ((self.parent is None or self.parent.parent is None) or self.parent.parent.parent is None) or self.parent.parent.parent.parent is None:
            return False
        if player == 1:
            index1 = self.state.index('1')
            index2 = self.state.index('2')
            old_index1 = self.parent.parent.state.index('1')
            old_index2 = self.parent.parent.state.index('2')
            very_old_index1 = self.parent.parent.parent.parent.state.index('1')
            very_old_index2 = self.parent.parent.parent.parent.state.index('2')
            forbidden = [7,8]
            if (index1 == old_index1 and index1 == very_old_index1 and index1 in forbidden) or (index2 == old_index2 and index2 == very_old_index2 and index2 in forbidden):
                return True
            else:
                return False
        elif player == 2:
            index8 = self.state.index('8')
            index9 = self.state.index('9')
            old_index8 = self.parent.parent.state.index('8')
            old_index9 = self.parent.parent.state.index('9')
            very_old_index8 = self.parent.parent.parent.parent.state.index('8')
            very_old_index9 = self.parent.parent.parent.parent.state.index('9')
            forbidden = [0,1]
            if (index8 == old_index8 and index8 == very_old_index8 and index8 in forbidden) or (index9 == old_index9 and index9 == very_old_index9 and index9 in forbidden):
                return True
            else:
                return False
    
    def terminal_test(self, player):
        if self.utility(player) != 0 or self.depth == 10:
            return True
        else:
            return False
        
    def __str__(self):
        return ('\n' + self.state[0] + self.state[1] + self.state[2] + '\n' + self.state[3] + self.state[4] + self.state[5] + '\n' + self.state[6] + self.state[7] + self.state[8] + '\n')
                
            
def minmax_pruning(node, player):

    def max_val(node, player, alpha= -float('inf'), beta=float('inf')):
        GameNode.count += 1
        if node.terminal_test(player):
            return node.utility(player)
        v = -float('inf')
        for child in EightPuzzleGame.expand(node, player):
            v = max(v, min_val(child, player, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def min_val(node, player, alpha= -float('inf'), beta=float('inf')):
        GameNode.count += 1
        if node.terminal_test(player):
            return node.utility(player)
        v = float('inf')
        for child in EightPuzzleGame.expand(node, 2 if player == 1 else 1):
            v = min(v, max_val(child, player, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    
    return max_val(node, player)
    




# Program excepts three arguments as requested in the project description.
if len(sys.argv) != 3:
    print("Usage: python part2.py <input_file> <output_file>")
    exit(1)


input_state = ''
agent = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        if len(input_state) == 9:
            agent = line.split()[0]
            continue
        line_numbers = ''.join(line.split())
        input_state += line_numbers

root = GameNode(input_state)
val = minmax_pruning(root, int(agent))

with open(sys.argv[2], 'w') as file:
    file.write('Value: ' + str(val) + '\n')
    file.write('Expanded: ' + str(GameNode.count - 1) + '\n')





                