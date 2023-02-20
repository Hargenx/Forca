#Defining globals. Note: Using globals is bad practice, use function arguments instead
chosenword = 'boot'
attempts = 4


def game():
  global chosenword
  global attempts

  #Create needed extra variables directly from input
  wordlen = len(chosenword)
  chosenwordlist = list(chosenword)

  tally = 1
  print("\nThe word to guess is....\n")
  print(chosenword)

  #Added whitespace for better wordlength visualisation
  display = "_ " * wordlen
  print(display)

  print(chosenwordlist)

  #This holds the letters that have been guessed already
  guessedletters = []

  while tally <= int(attempts):
    display = ''
    userchoice = input()

    if len(userchoice.strip()) == 1:
      #check if the guess is part of the word to guess
      if userchoice in chosenwordlist:
        # Check if letter has been guessed before
        if userchoice in guessedletters:
          print('You tried that letter already')
          continue
        else:
          # Add the guessed letter to the list of all guessed letters and create display
          guessedletters.append(userchoice)
          for i in range(wordlen):
            if chosenwordlist[i] in guessedletters:
              display += chosenwordlist[i]
            else:
              display += '_ '
      else:
        print("Wrong guess")
        tally = tally + 1

      print("\n" + display)

      if display == chosenword:
        tally = int(attempts) + 1
        print("Congratulations\nYou guessed the word correctly")

    else:
      print("Invalid input\nEnter only a single letter\n")
      print(display)

if __name__ == '__main__':
  game()