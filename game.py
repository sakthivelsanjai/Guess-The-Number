import random
def welcome():
    print("🎮<<<Welcome to Number Game>>>🎮")
    print("=========<<<<<>>>>>>=========")
def choose_level():
    print("Choose your level[1/2/3]"
          "\n1)Easy---> 7(Attempts)"
          "\n2)Medium---> 5(Attempts)"
          "\n3)Hard---> 3(Attempts)")
    try:
        level = int(input("Choose your level: "))
    except ValueError:
        print("You entered wrong value,Defaulting to Easy")
        return 1
    if level == 1:
        print("You Choose Easy😎")
        return 7
    elif level == 2:
        print("You Choose Medium🤔")
        return 5
    elif level == 3:
        print("You Choose Hard😤")
        return 3
    else:
        return 3

def game():
        guess_number=random.randint(1,20)
        attempts_allowed= choose_level()
        chances=0
        print("🚀 Game Starts 🏁")
        while chances < attempts_allowed:
            try:
                guess=int(input("Guess a number between 1 and 20: "))
            except ValueError:
                print("Please enter a valid number❌😢")
                continue
            chances+=1
            if guess < guess_number:
                    print("😢Sorry, your guess is too low 📉")
            elif guess > guess_number:
                print(" 😢Sorry, its higher than that of you 📈")
            else:
                print("🎉 You got it! 🏆")
                print("You found in",chances,"Attempts👏👏")
                break
        else:
            print("💀 Game Over! ❌")
            print("The correct number is ", guess_number)

def main():
    welcome()
    while True:
        game()
        again=input("Would you like to play again? Yes ✅ / No ❌").lower()
        if again !="yes":
            break
main()


