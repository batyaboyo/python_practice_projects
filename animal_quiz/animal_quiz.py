def check_guess(guess, answer):
    global score  
    still_guessing = True  
    attempt = 0  
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')  
            score = score + 3
            still_guessing = False              
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again >>')  
                attempt = attempt + 1  
        
        if attempt == 3:
            print('The correct answer is ' + answer) 
            
score = 0 
print('Guess the Animal') 
guess1 = input('Which animal is the King of the jungle? >> ') 
check_guess(guess1, 'lion')
guess2 = input('Which is the fastest land animal? >>') 
check_guess(guess2, 'cheetah') 
guess3 = input('Which is the largest animal on land? >> ') 
check_guess(guess3, 'elephant')
guess4 = input('Which animal is the most dangerous? >> ') 
check_guess(guess4, 'Tiger')
guess5 = input('Which is the tallest animal? >>') 
check_guess(guess5, 'girrafe') 
guess6 = input('Which animal is found in Australia ? >> ') 
check_guess(guess6, 'kangaroo')
print('Your score is ' + str(score))