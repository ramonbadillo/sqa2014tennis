# -*- coding: utf-8 -*-
class Match:
    score = []
    opcionset = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.textoganador = ""
        self.wonp1 = 0
        self.wonp2 = 0
        del self.score[:]
        self.score.append("0-0")
        self.ganadorinicial = "none"

    def score_set(self):
        self.ganador()
        return "{0} | {1}".format(self.textoganador, self.listascoreset())

    def iniciarganador(self, playerwon):
        if self.ganadorinicial == "none":
            self.ganadorinicial = playerwon

    def listascoreset(self):
        listascore = ""
        inicio = 0
        for index in self.score:
            if inicio == 0:
                listascore = index
                inicio += 1
            else:
                listascore = listascore + ", " + index
        return listascore

    def ordenarscoreganador(self, playerwon, scorej1, scorej2):
        self.iniciarganador(playerwon)
        if self.ganadorinicial == playerwon:
            return scorej1 + "-" + scorej2
        else:
            return scorej2 + "-" + scorej1

    def save_set_won(self, player):
        if(player == self.p1):
            self.wonp1 += 1
        else:
            self.wonp2 += 1

    def save_score_set(self, scorej1, scorej2, numberset, playerwon):
        if(numberset == "1st"):
            self.score[0] = self.ordenarscoreganador(
                playerwon, scorej1, scorej2)
        else:
            self.score.insert(self.opcionset.get(
                numberset), self.ordenarscoreganador(playerwon, scorej1, scorej2))

    def ganador(self):
        numeroaum = 1
        if int(self.pacted_sets) == 5:
            numeroaum = 2

        if((self.wonp1 + numeroaum) == int(self.pacted_sets)):
            self.textoganador = self.p1 + " defeated " + self.p2
        elif ((self.wonp2 + numeroaum) == int(self.pacted_sets)):
            self.textoganador = self.p2 + " defeated " + self.p1
        else:
            self.textoganador = self.p1 + " plays with " + self.p2