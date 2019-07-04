print("Q2) Suppose you have a sorted list of 256 names, and you're searching through it using binary search. What's the maximum number of steps it would take?")


def check_answer():
    user_answer = str(input("Please enter your answer for the question :: "))
    if user_answer == '8':
        print("Congo! You got that right!")
    else:
        try_again = input("Sorry, that's not right. Wanna give it a try again? y/n :: ")
        multi_try(try_again)
        
def multi_try(try_again):
    if try_again == 'y':
        check_answer()
    elif try_again == 'n':
        print("The right answer is 8 ---> log(256) with base 2.")
    else:
        print("Please enter 'y' or 'n' as response. Try again")
        check_answer()

check_answer()