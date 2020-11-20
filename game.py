from typing import List

class Game:
    def __init__(self, height: int, width: int, players: 'List[Game.Player]'):
        self.maxColumn = width - 1
        self.maxRow = height - 1
        self.players = players
        self.isFinished = False
        self.gameField = [
            ['o' for i in range(width)]
            for i in range(height)
        ]
    
    def visualizeField(self):
        print()
        for row in self.gameField:
            print('|'.join(row))
        print()
    
    def getPlayer(self, playerNum: int) -> 'Game.Player':
        if playerNum > (len(self.players) - 1): raise Exception(f'No player {playerNum}')
        return self.players[playerNum]

    def dropOnColumn(self, playerNum: int, column: int):
        if self.isFinished: raise Exception('Game is finished')
        if column < 0: raise Exception('Column can not be negative')
        if column > self.maxColumn: raise Exception(f'Column can not be more than {self.maxColumn}')

        currentRow = 0
        player = self.getPlayer(playerNum)
        if self.gameField[0][column] != 'o': raise Exception('Column is full')
        while True:
            if currentRow == self.maxRow: # we fall on bottom
                self.gameField[currentRow][column] = player.sign
                break

            if self.gameField[currentRow + 1][column] != 'o': # next row is filled
                self.gameField[currentRow][column] = player.sign
                break
                
            currentRow = currentRow + 1
        self._checkForWinning(currentRow, column, playerNum)

    def _checkForWinning(self, row: int, column: int, playerNum: int):
        player = self.getPlayer(playerNum)
        if self.gameField[row][column] != player.sign: raise Exception('Checking wrong cell')

        directions = [
            {'rowStep': 0, 'columnStep': 1},
            {'rowStep': 1, 'columnStep': 0},
            {'rowStep': 1, 'columnStep': 1},
            {'rowStep': 1, 'columnStep': -1}
        ]

        wonLine = None

        for d in directions:
            oneHalf = self._findInRow(row, column, d['rowStep'], d['columnStep'])
            secondHalf = self._findInRow(row, column, -d['rowStep'], -d['columnStep'])
            if (len(oneHalf) + len(secondHalf) + 1) == 4:
                wonLine = oneHalf + [(row, column)] + secondHalf
                break
        
        if wonLine is not None and len(wonLine) >= 4:
            for row, column in wonLine:
                self.gameField[row][column] = player.winSign
            self._finishGame(playerNum)

    
    def _findInRow(self, row: int, column: int, rowStep: int = 0, columnStep: int = 0): 
        if rowStep == 0 and columnStep == 0: return
        letter = self.gameField[row][column]
        currentRow = row
        currentColumn = column
        letters = []
        while True:
            if len(letters) > 0:
                currentRow, currentColumn = letters[-1]
            rowToCheck = currentRow + rowStep
            columnToCheck = currentColumn + columnStep

            if rowToCheck < 0 or rowToCheck > self.maxRow: break
            if columnToCheck < 0 or columnToCheck > self.maxColumn: break

            if self.gameField[currentRow + rowStep][currentColumn + columnStep] == letter:
                letters.append((rowToCheck, columnToCheck))
                continue
            else:
                break
        
        return letters
    
    def _finishGame(self, playerNum: int):
        self.isFinished = True
    
    def restart(self):
        for row in self.gameField:
            for i in range(len(row)):
                row[i] = 'o'
        self.isFinished = False

    class Player:
        def __init__(self, sign: str, winSign: str):
            if len(sign) != 1: raise Exception('sign must be one letter')
            if len(winSign) != 1: raise Exception('sign must be one letter')
            self.sign = sign
            self.winSign = winSign
