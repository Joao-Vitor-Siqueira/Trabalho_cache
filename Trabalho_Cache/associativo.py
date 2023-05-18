def inicializar_cache_associativa(nConjuntos):
    cache = []
    print('---------MENU DE OPERACOES---------')
    print('1. Numero de blocos: 1')
    print('2. Numero de blocos: 2')
    print('3. Numero de blocos: 4')
    print('4. Numero de blocos: 8')
    print('5. Numero de blocos 16')
    op = int(input('Digite a operacao a ser escolhida: '))
    match op:
        case 1:
            numeroBlocos = 1
        case 2:
            numeroBlocos = 2
        case 3:
            numeroBlocos = 4
        case 4:
            numeroBlocos = 8
        case 5:
            numeroBlocos = 16


    for i in range(0,nConjuntos):
        cache.append({})
        for j in range(0,numeroBlocos):
           cache[i][j] = -1
    return cache


def imprimir_cache(cache):
    print()
    for i in range(0,len(cache)):
        print("Conjunto:",(i+1),"\n")
        print("Pos Cache |Posição Memória")
        for key, value in cache[i].items():
            print("       ",key, "|", value)
        print("-------------------------------------------")

def inicializar_lru(nConjuntos):
    lru = {}
    for i in range(0,nConjuntos):
        lru[i] = -1
    return lru        

def mapeamento_associativo_lru(nConjuntos,pos_memoria):
    cache = inicializar_cache_associativa(nConjuntos)
    print("Cache inicial")
    print("Tamanho da Cache:",nConjuntos)
    imprimir_cache(cache)
    print()
    hits = 0
    misses = 0
    lru = inicializar_lru(nConjuntos)
    for i in range(0,pos_memoria):
        print("Linha",i,"| posição de memória desejada", pos_memoria[i])
        posCache = pos_memoria[i] % nConjuntos
        for j in range(0,len(cache[0])):







