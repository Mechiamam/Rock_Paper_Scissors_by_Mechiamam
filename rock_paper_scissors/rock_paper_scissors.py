from random import randint
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
win_counter = 0
draw_counter = 0
lose_counter = 0
while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
    computer_random_number = randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer chose {computer_move}")
    if player_move == rock and computer_move == rock \
        or player_move == paper and computer_move == paper \
        or player_move == scissors and computer_move == scissors:
        draw_counter += 1
        print("Draw!")
        question = input("Do you want to play again? ")
        if question == "Yes":
            computer_random_number = randint(1, 3)
            if computer_random_number == 1:
                computer_move = rock
            elif computer_random_number == 2:
                computer_move = paper
            else:
                computer_move = scissors
            continue
        elif question == "No":
            print(f"Scoreboard:\nNumber of won games: {win_counter}\n"
                  f"Number of lost games: {lose_counter}\n"
                  f"Number of draws: {draw_counter}")
            quit()
    elif player_move == rock and computer_move == paper \
        or player_move == paper and computer_move == scissors \
        or player_move == scissors and computer_move == rock:
        lose_counter += 1
        print("You lose!")
        question = input("Do you want to play again? ")
        if question == "Yes":
            computer_random_number = randint(1, 3)
            if computer_random_number == 1:
                computer_move = rock
            elif computer_random_number == 2:
                computer_move = paper
            else:
                computer_move = scissors
            continue
        elif question == "No":
            print(f"Scoreboard:\nNumber of won games: {win_counter}\n"
                  f"Number of lost games: {lose_counter}\n"
                  f"Number of draws: {draw_counter}")
            quit()
    else:
        win_counter += 1
        print("You win!")
        question = input("Do you want to play again? ")
        if question == "Yes":
            computer_random_number = randint(1, 3)
            if computer_random_number == 1:
                computer_move = rock
            elif computer_random_number == 2:
                computer_move = paper
            else:
                computer_move = scissors
            continue
        elif question == "No":
            print(f"Scoreboard:\nNumber of won games: {win_counter}\n"
                  f"Number of lost games: {lose_counter}\n"
                  f"Number of draws: {draw_counter}")
            quit()
