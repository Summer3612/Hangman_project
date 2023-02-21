import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=4):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(0,len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_letters=[]
       
        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")
        self.drawing(4)

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
     
        self.letter = letter.lower()
       
        if self.letter in self.word:
            for key, value in enumerate(self.word): 
                if value == self.letter:
                        self.word_guessed[key] = self.letter
            print (self.word_guessed)
            self.num_letters -= 1
            self.drawing(self.num_lives)
            
        else: 
            self.num_lives-=1
            print(f"{self.word_guessed}")
            self.drawing(self.num_lives)
            print (f"You have {self.num_lives} life/lives left.")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
       
        self.letter = input("enter a letter: ")
        
        if len(self.letter) > 1 :
            print ("Please, enter just one character")
        elif self.letter in self.list_letters:
            print(f"{self.letter} was already tried")
        elif not self.letter.isalpha():
            print ("This is not a valid letter") 

        else:
            self.list_letters.append(self.letter)
            self.check_letter(self.letter)
    
    def drawing (self,num_lives):
        num_lives = self.num_lives
        if num_lives ==4:
            print (" _____")
            print ("|     |")
            print ("|       ")
            print ("|       ") 
            print ("|       ")
            print ("|       ") 
            print ("|________")
            print ("|        |______                 0")
            print ("|               |______         /|\\")
            print ("|                      |______  / \\")
            print ("|_____________________________|")
        elif num_lives ==3 :
            print (" _____") 
            print ("|     |")
            print ("|       ")
            print ("|       ")
            print ("|       ")
            print ("|       ")
            print ("|________                 0")
            print ("|        |______         /|\\")
            print ("|               |______  / \\")
            print ("|                      |______")
            print ("|_____________________________|")
        elif num_lives==2:
            print (" _____")
            print ("|     |")
            print ("|       ")
            print ("|       ")
            print ("|        ")
            print ("|                  0")
            print ("|________         /|\\")
            print ("|        |______  / \\")
            print ("|               |______")
            print ("|                      |______")
            print ("|_____________________________|")
        elif num_lives==1:
            print (" ______") 
            print ("|      |")
            print ("|       ")
            print ("|       ")
            print ("|           0")
            print ("|          /|\\")
            print ("|________  / \\")
            print ("|        |______")
            print ("|               |______")
            print ("|                      |______")
            print ("|_____________________________|")
        elif num_lives==0: 
            print (" ______")
            print ("|      |")
            print ("|      0")
            print ("|     /|\\")
            print ("|     / \\")
            print ("|         ")
            print ("|________ ")
            print ("|        |______")
            print ("|               |______")
            print ("|                      |______")
            print ("|_____________________________|")
    

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=4)
  
    while game.num_lives>0 and game.num_letters>0:
        game.ask_letter()
    else: 
        if game.num_lives ==0:
            print(f"You ran out of lives. The word was {game.word}.")
        elif game.num_letters ==0:
            print (f"Congratulations, you won!The word was {game.word}.")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
