from user import User


class Player(User):

    def __init__(self):
        self.move = ''
        super().__init__()

    user_choice_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']




