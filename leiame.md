# Caixeiro Viajante
## Descrição
Foram implementados na linguagem Python os seguintes algoritmos:
* Algoritmo de Kruskal para encontrar caminhos mínimos
* Algoritmo heurístico do vizinho mais próximo para resolução do problema do Caixeiro Viajante

O código fonte está disponível [aqui](https://github.com/arthurmbandeira/tsp-grafos/).

## Execução
O arquivo principal da biblioteca é o [main.py](https://github.com/arthurmbandeira/tsp-grafos/blob/master/main.py) e deve ser executado com o seguinte comando:

``` $ python3 main.py ```

Foram definidos alguns testes baseados nas notas de aula da disciplina e estes se encontram na pasta [testes](https://github.com/arthurmbandeira/tsp-grafos/tree/master/testes).

O arquivo de teste deve estar no seguinte formato. A primeira linha informa o número de vértices do grafo, a segunda linha informa o número de arestas. Cada linha subsequente informa o par de vértices das arestas e o último elemento de cada linha indica o peso da aresta. Por exemplo: 

``` 
5
10
0 1 5
0 2 9
0 3 12
0 4 11
1 2 10
1 3 8
1 4 7
2 3 6
2 4 13
3 4 14
```

Quando solicitado pelo programa, insira o nome do arquivo presente na pasta testes com a extensão, por exemplo:

``` teste1.txt ```

Após isso siga as orientações do menu apresentado no console.

O código fonte está licenciado sob licença do [MIT](https://github.com/arthurmbandeira/tsp-grafos/blob/master/LICENSE).

### Arthur Manuel Bandeira
