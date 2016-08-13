#Arthur Manuel Bandeira - RA 67226

from Grafo import Grafo

G = Grafo()

def ler(G, file):
    line = file.readline()
    spt = line.split()
    x = (spt[0])
    y = (spt[1])
    z = (spt[2])
    if '.' in z:
        z = float(z)
    else:
        z = int(z)
    G.addAresta(x, y, z)
    G.addAresta(y, x, z)
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
    arquivo = input("Digite o nome do arquivo de entrada com a extensão (deve estar na pasta testes): ")
    arquivo = "testes/" + str(arquivo)
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

# Algoritmo de kruskal para árvore geradora mínima
def kruskal(G):
    total = 0
    mst = []
    for k in G:
        makeSet(k)
    arestas = list(G.getItens())
    arestas.sort(key=lambda x: x[1])
    for aresta in arestas:
        vertice1, vertice2 = aresta[0]
        vertice1 = G.getVertice(vertice1)
        vertice2 = G.getVertice(vertice2)
        if findSet(vertice1) != findSet(vertice2):
            union(vertice1, vertice2)
            mst.append(aresta[0])
            total += aresta[1]
    print("Total: " , total)
    return mst

# Algoritmo heurístico do caminho mais próximo
def tsp_nn(G, s):
    s = G.getVertice(s)
    C = [s]
    v = s
    nn = s
    menorPeso = float('Inf')
    pesoTotal = 0
    while len(C) != G.numVertices:
        for k in v.getAdj():
            if k not in C:
                if v.getPeso(k) < menorPeso:
                    menorPeso = v.getPeso(k)
                    nn = k
        pesoTotal += menorPeso
        menorPeso = float('Inf')
        C.append(nn)
        v = nn
    pesoTotal += C[-1].getPeso(s)
    C.append(s)
    return C, pesoTotal

#Menu de opções
def menu():
    print("Escolha uma das opcoes ou pressione 'q' para sair")
    print("[1] Arvore Geradora Minima - Kruskal")
    print("[2] Caixeiro Viajante - Algoritmo heuristico do vizinho mais proximo")
    print("[3] Imprimir Grafo")
    print("[4] Trocar arquivo")
    print("[q] Sair")

#Interação com o usuário
interfaceArquivo()
menu()
while True:
    teclado = input()
    if teclado == '1':
            caminho = kruskal(G)
            print("Arestas do caminho: ")
            print(caminho)
    elif teclado == '2':
        s = input("Informe o vertice inicial: ")
        print('\n')
        if s not in G.getVertices():
            print("Este vertice nao pertence ao grafo, tente novamente.")
        else:
            resposta, peso = tsp_nn(G, s)
            print("Caminho: ")
            for i in resposta:
                print(i.getID())
            print("Peso do caminho: ", peso)
    elif teclado == '3':
        imprimeGrafo(G)
    elif teclado == '4':
        del G
        G = Grafo()
        interfaceArquivo()
        imprimeGrafo(G)
    elif teclado == 'q':
        print("Tchau!")
        break
    else:
        menu()