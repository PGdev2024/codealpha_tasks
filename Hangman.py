#Hangman Game Implementation in Python
import random #random module imported to like choose 5 random words from list of predefined words 
predefined_words=[ #Predefined words list to store predefined words
    "planet", "window", "bridge", "castle", "forest", "hunter", "silver", "jungle", "pillow", "hammer", 
    "basket", "rocket", "mirror", "button", "ladder", "guitar", "shovel", "cotton", "butter", "temple",
    "dragon", "circle", "branch", "marble", "candle", "pencil", "magnet", "jacket", "socket", "target",
    "screen", "thread", "garden", "pigeon", "saddle", "closet", "helmet", "bucket", "school", "banana",
    "folder", "parrot", "monkey", "coffin", "curtain", "gloves", "puzzle", "camera", "animal", "border",
    "donkey", "signal", "tunnel", "ticket", "bottle", "wallet", "garage", "handle", "powder", "kettle",
    "frozen", "pocket", "rabbit", "pepper", "cradle", "cactus", "drawer", "napkin", "beacon", "carpet",
    "anchor", "valley", "prince", "market", "shelter", "engine", "parcel", "museum", "oxygen", "glider",
    "ballot", "throne", "apples", "across", "hunger", "replay", "salmon", "velvet", "grapes", "sneeze",
    "breeze", "laptop", "switch", "buckle", "flight", "basketball", "muffin", "cobweb", "lantern", "whistle"
]
game_words=[random.choice(predefined_words) for index in range(5)] #game words list to choose and store 5 random words from list of predefined words
print("Welcome to the game of Hangman ! Type Hangman to start the game") 
start_key=input() #Taking user input 
def HangmanGame(start_key): #HangmanGame function defined to like implement reusability,modularity and like restart feature if invalid input is entered at the before the start of the game
    global game_words
    if start_key=="Hangman" or start_key=="hangman": #To impelement game start functionality by hangman word user input
      max_incorrect_guesses=6 #To store maximum incorrect guesses whicha are 6
      incorrect_guesses,correct_guesses=0,0 #Defining incorrect guesses and correct guesses and setting them 0 at the beginning of the game
      word_index=0 #word index used to iterate over the words in game words list
      while incorrect_guesses<max_incorrect_guesses and correct_guesses<5: #While loop to ensure that game runs till incorrect guesses are less than maximum incorrect guesses or till the user guesses all the words correctly and wins
          guess_word=input("Guess the word ") #Taking user's guessed word for input
          if guess_word.lower()==game_words[word_index]: #Checking if user's word matches the current word in the game words list and also converting it into lowercase before hand for safety and better input handling
              print("Correct Guess!") 
              correct_guesses+=1 #correct guesses incremented by 1 upon correct guess by the user
              word_index+=1 #word index incremented if guessed word is correct to move to the next word
          elif guess_word=="Q" or guess_word=="q": #Implementing exit feature in the game by Q or q input from the user
              print(f"Your Score: {correct_guesses}/{5}")
              print("Game Exited")
              exit() #Exiting the game if user inputs Q or q
          else:
              print("Incorrect Guess! Try Again") 
              incorrect_guesses+=1 #incorrect guesses incremented by 1 upon incorrect guess by the user
      if incorrect_guesses==max_incorrect_guesses:  #Checking whether has user run out of guesses 
          print(f"Sorry,but you are out of guesses.The word was {game_words[word_index]} ")
          print(f"Your Score: {correct_guesses}/{5}") #Printing score of the user 
      elif correct_guesses==5: #Checking whether user has won
          print("You Won!") 
    else: #Handling invalid response and like prompting the user to try again by restarting by again calling the function
      print("You have entered invalid input! Try again") 
      start_key=input() #Again taking input after user has entered invalid input to start the game
      HangmanGame(start_key) #Again calling the Hangman Game function to like restart upon invalid input by the user
HangmanGame(start_key) #Calling the function for the first time to implement the starting of game functionality
