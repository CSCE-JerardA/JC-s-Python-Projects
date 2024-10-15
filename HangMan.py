import tkinter as tk
import random
from string import ascii_uppercase
wordList = ["python", "javascript"]



class HangmanGame(object):

    def __init__(self, root, readFile):
        self.readFile = open("wordlist.txt","r")
        self.tLabel = tk.Label(master = root, text = "Hangman", height = 3)
        self.tLabel.grid(row = 0, column = 0, columnspan = 13, sticky = "news")
        for line in self.readFile:
            self.wordList = [word.strip() for word in self.readFile()]
            for word in self.wordList:
                if len(word) <= 5 and len(word) >= 10:
                    wordList.append(word)



        self.secretWord = random.choice(wordList)
        self.wLabel = tk.Label(master = root, text = "_ "*len(self.secretWord), height = 3)
        self.wLabel.grid(row = 1, column = 0, columnspan = 13, sticky = "news")
        for n , letter in enumerate(ascii_uppercase):
            b = tk.Button(master = root, text = letter, command= lambda x = letter: self.process_click(x))
            b.grid(row = 2 + n // 13, column = n % 13)
    def process_click(self, letter):
        print(letter)
window = tk.Tk()
game = HangmanGame(window,"wordlist.txt")
window.mainloop()