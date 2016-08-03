#Arthur Manuel Bandeira - RA 67226

import heapq

from Grafo import Grafo
# from PriorityQueue import PriorityQueue


G = Grafo()

def ler(G, file):
    line = file.readline()
    spt = line.split()
    x = (spt[0])
    y = (spt[1])
    z = int(spt[2])
    G.addAresta(x, y, z)
    return G

def imprimeGrafo(G):
    for v in G:
        for w in v.getAdj():
            print(v.getID(), w.getID(), v.getPeso(w))
    print('\n')

def abreArquivo(path):
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        print("Arquivo inexistente ou inacessivel na pasta testes, tente novamente...")
        interfaceArquivo()
        return

    nroVertices = int(f.readline())
    nroArestas = int(f.readline())
    for i in range(nroArestas):
        ler(G, f)

    f.close()

def interfaceArquivo():
    # arquivo = input("Digite o nome do arquivo de entrada (deve estar na pasta testes): ")
    arquivo = "testeprim"
    arquivo = "testes/" + str(arquivo) + ".txt"
    abreArquivo(arquivo)

def makeSet(vertice):
	vertice.pai = vertice
	vertice.ranking = 0

def findSet(vertice):
	if (vertice.getPai() != vertice):
		vertice.pai = findSet(vertice.getPai())
	return vertice.getPai()

def union(vertice1, vertice2):
	raiz1 = findSet(vertice1)
	raiz2 = findSet(vertice2)
	if raiz1 != raiz2:
		if (raiz1.getRanking() > raiz2.getRanking()):
			raiz2.pai = raiz1
		else:
			raiz1.pai = raiz2
			if (raiz1.getRanking() == raiz2.getRanking()):
				raiz2.ranking += 1

def kruskal(G):
	# raiz = G.getVertice(raiz)
	total = 0
	for k in G:
		makeSet(k)
	arestas = list(G.getItens())
	arestas.sort(key=lambda x: x[1])
	print(arestas)
	for aresta in arestas:
		vertice1, vertice2 = aresta[0]
		vertice1 = G.getVertice(vertice1)
		vertice2 = G.getVertice(vertice2)
		if findSet(vertice1) != findSet(vertice2):
			union(vertice1, vertice2)
			total += aresta[1]
	print("Total: %d" % total)


interfaceArquivo()
s = input("Informe o vertice inicial: ")
print('\n')
if s not in G.getVertices():
    print("O vertice inicial nao pertence ao grafo, tente novamente.")
else:
	imprimeGrafo(G)
	kruskal(G)
