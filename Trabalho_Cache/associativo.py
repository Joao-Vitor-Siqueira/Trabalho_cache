import queue

def inicializar_cache_associativa(nConjuntos,nBlocos):
    cache = []
    for i in range(0,nConjuntos):
        cache.append({})
        for j in range(0,nBlocos):
           cache[i][j] = -1
    return cache


def imprimir_cache(cache,fifo):
    print()
    for i in range(0,len(cache)):
        print("Conjunto:",(i))
        print("Fifo: ",end="")
        fifo[i] = imprimir_queue(fifo[i])
        print("Pos Cache |Posição Memória")
        for key, value in cache[i].items():
            print("       ",key, "|", value)
        print("-------------------------------------------")


def imprimir_queue(q):
    newQueue = queue.Queue()
    print("[",end="")
    while not q.empty():
        item = q.get()
        print(item,end=",")
        newQueue.put(item)
    print("]")
    return newQueue

def inicializar_fifo(nConjuntos):
    fifo = []
    for i in range(0,nConjuntos):
        q = queue.Queue()
        fifo.append(q)
    return fifo


def mapeamento_associativo_fifo(nConjuntos,nBlocos,pos_memoria):
    cache = inicializar_cache_associativa(nConjuntos,nBlocos)
    fifo = inicializar_fifo(nConjuntos)
    print("Cache inicial")
    print("Tamanho da Cache:",nConjuntos)
    imprimir_cache(cache,fifo)
    print()
    hits = 0
    misses = 0
    for i in range(0,len(pos_memoria)):
        pos_cache = pos_memoria[i] % nConjuntos #calculo de posição na cache
        print("Linha",i,"| posição de memória desejada", pos_memoria[i])
        for j in range(0,nConjuntos):  #loop por cada bloco no conjunto
            if cache[pos_cache][j] == pos_memoria[i]:
                print("Status: Hit")
                hits += 1
                break
            else: 
                if cache[pos_cache][j] == -1:  #cache com vagas disponíveis
                    print("Status: Miss")
                    misses += 1
                    cache[pos_cache][j] = pos_memoria[i]
                    fifo[pos_cache].put(j)
                    break
                elif -1 not in cache[pos_cache].values() and j == fifo[pos_cache].queue[0]: #cache cheia
                    print("Status: Miss")
                    misses += 1
                    cache[pos_cache][fifo[pos_cache].get()] = pos_memoria[i]
                    fifo[pos_cache].put(j) 
                    break
                else:
                    continue
        print("Tamanho da Cache:",nConjuntos)
        imprimir_cache(cache,fifo)
        print()
    
    taxa_acertos = (100 * hits) / len(pos_memoria)
    print("Memórias acessadas:", len(pos_memoria))
    print("Número de hits:", hits)                      
    print("Número de misses:", misses)
    print("Taxa de acertos (hits): ",format(taxa_acertos,".2f"),"%\n-------------------------------------------------------\n")
            
         

mapeamento_associativo_fifo(2,2,[1,3,1,5,7])                                                       





                








