import random
L_words = [ "Algorithm","Binary", "Compiler","Debugger", "Encryption","Firewall", "Hardware", "Internet",
    "JavaScript", "Keyboard", "Malware", "Network","Processor", "Query", "Router", "Software","Terabyte", 
    "Interface", "Virtualization","Wireless"]

word = random.choice(L_words)
word=word.upper()

letters = []
for i in word:
    if i not in letters:
        letters.append(i.upper())

correct_guess = []
wrong_guess = []
n=6 #number of tries left
answer = ['-']*len(word)
ans_str = ' '.join(answer)
while n>0:
    print("\n")
    print("Currently guessed word:",ans_str)
    print("Number of guesses remaining: ",n)
    if len(wrong_guess+correct_guess)==0:
        print("Already guessed letters: \n")
    else:
        print("Already guessed letters: ",wrong_guess+correct_guess)

    guess = input("Enter an alphabet to guess: ")
    guess=guess.upper()

    if guess.isalpha() == False or len(guess)!=1:
        print("Invalid input! Please enter a single alphabet that you'd like to guess\n")
        continue

    if (guess in correct_guess) or (guess in wrong_guess):
        print("Already guessed this letter, try again...\n")

    elif (guess not in letters):
        print("Wrong guess!")
        wrong_guess.append(guess)
        n=n-1
        continue

    elif (guess in letters):
        letters.remove(guess)
        correct_guess.append(guess)
        for i in range(len(word)):
            if word[i]==guess:
                answer[i]=guess
        ans_str = ' '.join(answer)
        if '-' in answer:
            continue
        else:
            break
if n==0:
    print("You lost! The word to be guessed was ",word)
else:
    print("Congratulations!! The word you guessed was ",word)




