# -*- coding: utf-8 -*-
"""
Al inicio del juego cómo debe de estar el score?
>>> Game().score()
[0, 0]

Cuando un jugador anota
>>> Game().scores(1).score()
[15, 0]

Cuando un jugador anota 3 veces seguidas
>>> Game().scores(1).scores(1).scores(1).score()
[40, 0]

Cuando un jugador anota 4 veces seguidas
>>> Game().scores(1).scores(1).scores(1).scores(1).score()
['wins!', 'loses']

Cuando el OTRO jugador anota 4 veces seguidas
>>> Game().scores(2).scores(2).scores(2).scores(2).score()
['loses', 'wins!']


Cuando el otro jugador le empata
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
['deuce', 'deuce']

Cuando estan empatados y uno obtiene la ventaja
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score()
['ads', '']

Cuando después de tener la ventaja vuelven a empatar
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).score()
['deuce', 'deuce']

Cuando obtiene la ventaja y además anota otro punto
>>> Game().scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(1).score()
['wins!', 'loses']


"""


class Game:

    def __init__(self):
        self._scores = [0, 0]

    def score(self):
        calls = [0, 15, 30, 40, 'game']
        isAThie = (self._scores[0] == self._scores[1])
        if isAThie and self._scores[0] >= 3:
            return ['deuce', 'deuce']
        elif self._scores[0] >= 4 or self._scores[1] >= 4:
            callsUp40 = {1: ['ads', ''], -1: ['', 'ads'],
                         2: ['wins!', 'loses'], -2: ['loses', 'wins!'],
                         3: ['wins!', 'loses'], -3: ['loses', 'wins!'],
                         4: ['wins!', 'loses'], -4: ['loses', 'wins!']}
            return callsUp40[self._scores[0] - self._scores[1]]
        else:
            return [calls[self._scores[0]], calls[self._scores[1]]]

    def scores(self, player):
        iPlayer = player - 1
        self._scores[iPlayer] += 1
        return self
