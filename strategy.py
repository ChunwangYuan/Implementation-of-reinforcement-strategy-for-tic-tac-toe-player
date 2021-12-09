import random
import copy

class Q_learning():
    def __init__(self):
        self.learning_rate = 0.2
        self.decay = 0.8
        self.exploratory_rate = 0.1
        self.states = {}
        self.states_history = []
    def selectMove(self, availableMoves, board, playerValue):
        board=board.board
        probability = random.uniform(0, 1)
        if probability <= self.exploratory_rate:
            bestMove = availableMoves[random.randrange(0, len(availableMoves))]
        else:
            maxValue = float("-inf")
            bestMove = availableMoves[0]
            for availableMove in availableMoves:
                # get a copy of a board
                boardCopy = copy.deepcopy(board)
                boardCopy[availableMove[0]][availableMove[1]] = playerValue
                value = self.states.get(self.computeHash(boardCopy)) if self.states.get(
                    self.computeHash(boardCopy)) else 0
                if value > maxValue:
                    maxValue = value
                    bestMove = availableMove
        # Remember this state
        boardCopy = copy.deepcopy(board)
        boardCopy[bestMove[0]][bestMove[1]] = playerValue
        self.states_history.append(self.computeHash(boardCopy))
        return bestMove

    def computeHash(self, board):
        """Rearrange the board matrix as a single vector of 9 elements and convert it to string"""
        return str(board)


    def reward(self, rewardValue):
        for stateHash in reversed(self.states_history):
            if self.states.get(stateHash) is None:
                self.states[stateHash] = 0
            self.states[stateHash] += self.learning_rate * (self.decay * rewardValue - self.states[stateHash])
            rewardValue = self.states[stateHash]











class Random_strategy():
    def random_move(self, available_moves):
        return available_moves[random.randrange(0,len(available_moves))]

if __name__=='__main__':
    r=Random_strategy()
    f=r.random_move([(1,2),(0,0),(1,1)])
    print(f)



