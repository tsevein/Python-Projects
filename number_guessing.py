import random

def add_to_attempts_record(added_record):
    attempts_record.append(added_record)


def show_highest_score():
    highest_score = min(attempts_record)
    print("\nHighest Score: {}".format(highest_score))    


def show_intro():
    text = "======> Welcome to the Number Guessing Game! <======"
    text_len = len(text)
    print("-" * text_len)
    print(text)
    print("-" * text_len + "\n")


def show_outro():
    text = "======> Until next time! <======"
    text_len = len(text)
    print("\n" + "-" * text_len)
    print(text)
    print("-" * text_len)


attempts_record = []


def start_game():
    correct_number = random.randint(0, 10)
    attempts_count = 1
    if attempts_record:
        show_highest_score()
    while True:
        try:
            players_guess = int(input("Please enter a number between 0 and 10: "))
            if players_guess > 10:
                raise ValueError("Please enter a number within the range.")
            if players_guess < 0:
                raise ValueError("Please enter a number within the range.")    
        except ValueError as err:
            print("Invalid input. {} Try again.".format(err))
        else:
            if players_guess == correct_number:
                try:
                    invite = input("\nGot it!\nIt took you {} attempts.\nFeeling like playing again? Yes/No ".format(attempts_count))  
                except ValueError:
                    print("Invalid input. Try again.")
                else:            
                    if invite.lower() == "no":
                        show_outro()    
                        break
                    if invite.lower() == "yes":
                        add_to_attempts_record(attempts_count)
                        start_game()
                        break         
            elif players_guess > correct_number:
                print("It's lower!")
                attempts_count += 1
                continue
            elif players_guess < correct_number:
                print("It's higher!")
                attempts_count += 1
                continue  
    print()   
show_intro()
start_game()