import random

def pickRandomNum():
    
    num_ls = []

    for i in range(1,101):
        num_ls.append(i)
    
    num = random.choice(num_ls)

    return num


def boundHint(num):

    if num < 50:
        print('The number is between 1 and 50')

    else:
        print('The number is between 50 and 100')

def evenOrOdd(num):

    if num % 2 == 0:
        print('The number is even')

    else:
        print('The number is odd')

def guessIsTooBigOrSmall(guess_num, correct_num):

    if guess_num > correct_num:
        print('The number is less than your last guess')

    elif guess_num < correct_num:
        print('The number is greater than your last guess')

def main():

    correct_num = pickRandomNum()
    curr_guess = 0
    num_of_guesses = 0
    score = 100

    print('I have picked a number between 1 and 100. Try to guess what it is. You have 10 tries.')
    
    while (num_of_guesses <= 10):

        if correct_num == curr_guess: 

            print('Congratulations! You guessed the right number!')
            score = score - (num_of_guesses * 10)
            print(f'Score: {score}')
            break

        else:
            curr_guess = int(input('Your guess: '))
            num_of_guesses +=1

            if num_of_guesses == 3 and correct_num != curr_guess:

                print('Here is a hint: ')
                boundHint(correct_num)

            elif num_of_guesses == 5 and correct_num != curr_guess:
                print('Here is a hint: ')
                evenOrOdd(correct_num)

            elif num_of_guesses >= 7 and correct_num != curr_guess:
                guessIsTooBigOrSmall(curr_guess, correct_num)

            if abs(curr_guess - correct_num) <= 10 and correct_num != curr_guess:
                print('Getting close! Your guess is within 10 numbers away.')


    if (num_of_guesses > 10):
        print('Sorry you ran out of guesses')
        print(f'The correct answer is {correct_num}')
        score = 0
        print(f'Score: {score}')


if __name__ == "__main__":
    main()
    


