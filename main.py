from game import Game
from consoleGame import ConsoleGame

player1 = Game.Player('x', 'X')
player2 = Game.Player('z', 'Z')

twoPlayerGame = Game(6, 7, [player1, player2])

twoPlayerConsoleGame = ConsoleGame(twoPlayerGame)

twoPlayerConsoleGame.run()
