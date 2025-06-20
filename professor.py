import random

def main():
    level = get_level()
    score = simulate_game(level)
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError("Level must be 1, 2, or 3.")
            return level
        except ValueError:
            print("Invalid input")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level.")

def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def simulate_game(level):
    count_round = 1
    score = 0
    all_numbers = []

    while count_round <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        all_numbers.append(x)
        all_numbers.append(y)

        response = simulate_round(x, y)
        if response:
            score += 1
        count_round += 1

    print(all_numbers)
    return score

if __name__ == "__main__":
    main()
