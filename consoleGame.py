from game import Game

class ConsoleGame:
    def __init__(self, game: Game):
        self.game = game
    
    def run(self):
        print('New game started')
        self.game.visualizeField()
        currentPlayerNum = 0
        maxPlayerNum = len(self.game.players) - 1
        while True:
            print('#######################################')
            column = self._getColumnToDrop(currentPlayerNum)
            try:
                self.game.dropOnColumn(currentPlayerNum, column)
            except Exception as e:
                print('Unknown error, try again or restart application')
                continue
                
            if self.game.isFinished:
                self.game.visualizeField()
                answer = self._getFinishedAnswer(currentPlayerNum)
                if answer == 'restart':
                    self.game.restart()
                    self.game.visualizeField()
                    currentPlayerNum = 0
                    continue

                if answer == 'exit': return
            
            self.game.visualizeField()
            if currentPlayerNum == maxPlayerNum:
                currentPlayerNum = 0
            else:
                currentPlayerNum = currentPlayerNum + 1

    def _getColumnToDrop(self, playerNum: int) -> int:
        print(f'Player {playerNum + 1}, type column number to drop (1 - {self.game.maxColumn + 1})')
        while True:
            answer = input()
            if not answer.isdecimal():
                print('Invalid format')
                continue
            value = int(answer)
            if value < 1 or value > self.game.maxColumn + 1:
                print(f'Column must be from 1 to {self.game.maxColumn + 1}')
                continue
            return value - 1

    def _getFinishedAnswer(self, playerNum):
        print(f'Game is finished, player {playerNum + 1} won, type restart to restart, or exit to exit')
        appropriateAnswers = ['restart', 'exit']
        while True:
            answer = input()
            if answer in appropriateAnswers:
                return answer
            else:
                print('Invalid answer, type restart or exit')
