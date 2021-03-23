from user import User


class Player(User):

    def __init__(self):
        super().__init__()
        self.name = input('Please enter your name.')
        self.move = ''
    user_choice_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

