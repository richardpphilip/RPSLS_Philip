from user import User


class Player(User):



    def __init__(self):
        self.move = input("what move would you like to play?")
        super().__init__()

    user_choice_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def user_move(self):
        if self.move == 'rock':
            pass
        if self.move == 'paper':
            pass
        if self.move == 'scissors':
            pass
        if self.move == 'lizard':
            pass
        if self.move == 'spock':
            pass



