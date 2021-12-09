from strategy import Random_strategy
class Player:
    def __init__(self, strategy, player_value):
        self.player_value= player_value
        self.strategy= strategy
        if strategy== 'Random_strategy':
            self.game_plan='RANDOM_STRATEGY'
        else:
            self.game_plan= 'Q_LEARNING'

    def get_player_value(self):
        return self.player_value
    def move(self, available_move, board):
        if self.strategy=='Random_strategy':
            r_strategy= Random_strategy()
            random_move= r_strategy.random_move(available_move)
            return random_move
        else:
            return self.strategy.selectMove(available_move, board, self.player_value)

    def reward(self, reward_value):
        if self.strategy!='Random_strategy':
            self.strategy.reward(reward_value)
