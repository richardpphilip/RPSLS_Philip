from computer import Computer
from player import Player
import random

person_player = Player()
print('if you have a second player, please enter their name, otherwise press enter')
person_player2 = Player()
computer_player = Computer()


def decide_game():
    game_question = input("do you want to play two player or one player? type two for two or one for one")
    while game_question != 'one' or game_question != 'two':

        if game_question == 'one':
            play_game_one_person()
            break

        elif game_question == 'two':
            play_game_two_people()
            break
        else:
            print('that was not a correct response.  Please choose one or two.')
            game_question = input("do you want to play two player or one player? type two for two or one for one")


def game_turn_one_person():
    computer_player.move = Player.user_choice_list[random.randint(0, 4)]
    person_player.move = input(f"{person_player.name} what move do you want to play?")

    # rock
    if computer_player.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[
        2] or computer_player.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[3]:
        computer_player.win_counter += 1
        print(f'{computer_player.move} beat {person_player.move}, {computer_player.name} wins this round')
    elif computer_player.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[
        1] or computer_player.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[4]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {computer_player.move}, {person_player.name} wins this round.')
    elif computer_player.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[0]:
        print(f'{person_player.move} tied {computer_player.move}, no points awarded')
        # paper
    elif computer_player.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[
        0] or computer_player.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[4]:
        computer_player.win_counter += 1
        print(f'{computer_player.move} beat {person_player.move}, {computer_player.name} wins this round')
    elif computer_player.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[
        3] or computer_player.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[2]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {computer_player.move}, {person_player.name} wins this round.')
    elif computer_player.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[1]:
        print(f'{person_player.move} tied {computer_player.move}, no points awarded')
        # scissors
    elif computer_player.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[
        1] or computer_player.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[3]:
        computer_player.win_counter += 1
        print(f'{computer_player.move} beat {person_player.move}, {computer_player.name} wins this round')
    elif computer_player.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[
        4] or computer_player.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[0]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {computer_player.move}, {person_player.name} wins this round.')
    elif computer_player.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[2]:
        print(f'{person_player.move} tied {computer_player.move}, no points awarded')
        # lizard
    elif computer_player.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[
        1] or computer_player.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[4]:
        computer_player.win_counter += 1
        print(f'{computer_player.move} beat {person_player.move}, {computer_player.name} wins this round')
    elif computer_player.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[
        0] or computer_player.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[2]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {computer_player.move}, {person_player.name} wins this round.')
    elif computer_player.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[3]:
        print(f'{person_player.move} tied {computer_player.move}, no points awarded')
        # spock
    elif computer_player.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[
        0] or computer_player.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[2]:
        computer_player.win_counter += 1
        print(f'{computer_player.move} beat {person_player.move}, {computer_player.name} wins this round')
    elif computer_player.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[
        1] or computer_player.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[3]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {computer_player.move}, {person_player.name} wins this round.')
    elif computer_player.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[4]:
        print(f'{person_player.move} tied {computer_player.move}, no points awarded')
    else:
        print('that is not a valid response.  Please pick from the correct options.')


def game_turn_two_people():
    person_player.move = input(f" {person_player.name} what move do you want to play?")
    person_player2.move = input(f" {person_player2.name} what move do you want to play?")

    # rock
    if person_player2.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[
        2] or person_player2.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[3]:
        person_player2.win_counter += 1
        print(f'{person_player2.move} beat {person_player.move}, {person_player2.name} wins this round')
    elif person_player2.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[
        1] or person_player2.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[4]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {person_player2.move}, {person_player.name} wins this round.')
    elif person_player2.move == Player.user_choice_list[0] and person_player.move == Player.user_choice_list[0]:
        print(f'{person_player.move} tied {person_player2.move}, no points awarded')
        # paper
    elif person_player2.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[
        0] or person_player2.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[4]:
        person_player2.win_counter += 1
        print(f'{person_player.move} beat {person_player.move}, {person_player2.name} wins this round')
    elif person_player2.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[
        3] or person_player2.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[2]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {person_player2.move}, {person_player.name} wins this round.')
    elif person_player2.move == Player.user_choice_list[1] and person_player.move == Player.user_choice_list[1]:
        print(f'{person_player.move} tied {person_player2.move}, no points awarded')
        # scissors
    elif person_player2.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[
        1] or person_player2.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[3]:
        person_player2.win_counter += 1
        print(f'{person_player2.move} beat {person_player.move}, {person_player2.name} wins this round')
    elif person_player2.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[
        4] or person_player2.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[0]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {person_player2.move}, {person_player.name} wins this round.')
    elif person_player2.move == Player.user_choice_list[2] and person_player.move == Player.user_choice_list[2]:
        print(f'{person_player.move} tied {person_player2.move}, no points awarded')
        # lizard
    elif person_player2.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[
        1] or person_player2.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[4]:
        person_player2.win_counter += 1
        print(f'{person_player2.move} beat {person_player.move}, {person_player2.name} wins this round')
    elif person_player2.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[
        0] or person_player2.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[2]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {person_player2.move}, {person_player.name} wins this round.')
    elif person_player2.move == Player.user_choice_list[3] and person_player.move == Player.user_choice_list[3]:
        print(f'{person_player.move} tied {person_player2.move}, no points awarded')
        # spock
    elif person_player2.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[
        0] or person_player2.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[2]:
        person_player.win_counter += 1
        print(f'{person_player2.move} beat {person_player.move}, {person_player2.name} wins this round')
    elif person_player2.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[
        1] or person_player2.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[3]:
        person_player.win_counter += 1
        print(f'{person_player.move} beat {person_player2.move}, {person_player.name} wins this round.')
    elif person_player2.move == Player.user_choice_list[4] and person_player.move == Player.user_choice_list[4]:
        print(f'{person_player.move} tied {person_player2.move}, no points awarded')
    else:
        print('that is not a valid response.  Please pick from the correct options.')


def welcome_to_game():
    print('Welcome to rock, paper, scissors, lizard, spock!')

    # explain the rules


def explain_rules():
    print(' The rules are as follows:'
          ' Rock crush Scissors'
          ' Rock crushes Lizard'
          ' Paper covers Rock'
          ' Lizard poisons Spock'
          ' Spock smashes Scissors'
          ' Scissors decapitates Lizard'
          ' Lizard eats Paper'
          ' Paper disproves Spock'
          ' Spock vaporizes Rock'
          ' choose your move wisely')


def play_game_one_person():
    while computer_player.win_counter < 2 or person_player.win_counter < 2:
        game_turn_one_person()
        if computer_player.win_counter == 2:
            print(f' {computer_player.name} has won the game! ')
            break
        if person_player.win_counter == 2:
            print(f'  {person_player.name} has won the game!')
            break


def play_game_two_people():
    while person_player2.win_counter < 2 or person_player.win_counter < 2:
        game_turn_two_people()
        if person_player2.win_counter == 2:
            print(f' {person_player2.name} has won the game! ')
            break
        if person_player.win_counter == 2:
            print(f'  {person_player.name} has won the game!')
            break


def run_game():
    welcome_to_game()
    explain_rules()
    decide_game()

# give user option to pick a move
# randomize computer players turn
# calculate who wins
# keep track
# display winner and loser when winner gets two victories
