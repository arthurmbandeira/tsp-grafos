from collections import OrderedDict

class Vertice:
    """docstring for Vertice"""
    def __init__(self, chave):
        self.id = chave
        self.cor = ""
        self.pai = None
        self.adj = OrderedDict()
        self.d = 0
        self.f = 0
        self.nivel = 0
        self.ranking = 0

    def addVizinho(self, vizinho, peso = 0):
        self.adj[vizinho] = peso

    def getAdj(self):
        return self.adj.keys()

    def getID(self):
        return self.id

    def getCor(self):
        return self.cor

    def getPai(self):
        if (self.pai):
            return self.pai
        else:
            return None

    def getPeso(self, vizinho):
        if (self.adj[vizinho]):
            return self.adj[vizinho]
        else: return None

    def getTermino(self):
        return self.f

    def getNivel(self):
        return self.nivel

    def getRanking(self):
        return self.ranking

    # def __lt__(self, other):
    #     return self.nivel < other.nivel