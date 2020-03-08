import numpy as np

numberOfPieces = 7
mapSize = 4
numberOfDices = 4

class Dice:
    def throwDices(self):
        dices = np.random.randint(0,2,numberOfDices)
        return (sum(dices))

class Map:
    def __init__(self):
        self.warZone=np.zeros((mapSize), dtype= int)
class Player:
    def __init__(self, number):
        self.outPieces = 0
        self.pieces = numberOfPieces
    def killAPiece(self):
        self.pieces += 1
    def placeAPiece(self):
        self.pieces -= 1
    def getAPieceOut(self):
        self.outPieces += 1
class Game:
    def __init__(self):
        self.Map = Map()
        self.players = [Player(1), Player(2)]
        self.turn = 1
        self.dice = Dice()

    def opositeTurn(self):
        if(self.turn==1):
            return 2
        else:
            return 1

    def round(self):
        while(self.players[0].outPieces<numberOfPieces and self.players[1].outPieces<numberOfPieces):
            print(f" Table {self.Map.warZone} Player 1: left- {self.players[0].pieces} out- {self.players[0].outPieces} Player 2: left- {self.players[1].pieces} out- {self.players[1].outPieces}")
            value = self.dice.throwDices()
            if(value != 0):
                if(self.Map.warZone[value-1] != self.turn and self.players[self.turn-1].pieces>0):
                    if(self.Map.warZone[value-1]!=0):
                        self.players[self.opositeTurn()-1].killAPiece()
                    self.Map.warZone[value-1] = self.turn
                    self.players[self.turn-1].placeAPiece()
                else:
                    for i in range(mapSize):
                        if(self.Map.warZone[i]==self.turn and i+value >= mapSize):
                            self.Map.warZone[i]=0
                            self.players[self.turn-1].getAPieceOut()
                            break
            self.turn = self.opositeTurn()
        print(f" Table {self.Map.warZone} Player 1: left- {self.players[0].pieces} out- {self.players[0].outPieces} Player 2: left- {self.players[1].pieces} out- {self.players[1].outPieces}")
        print(f" Player {self.opositeTurn()} is the winner")
ga = Game()
ga.round()
