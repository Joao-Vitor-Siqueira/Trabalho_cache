def inicializar_cache(tamanho_cache):
    cache = {}
    for i in range(0,tamanho_cache):
        cache[i] = -1
    return cache


def imprimir_cache(cache):
    print("Pos Cache |Posição Memória")
    for key, value in cache.items():
      print("       ",key, "|", value)


def mapeamento_direto(tamanho_cache,pos_memoria):
    cache = inicializar_cache(tamanho_cache)
    print("Cache inicial")
    print("Tamanho da Cache:",tamanho_cache)
    imprimir_cache(cache)
    print()
    hits = 0
    misses = 0
    for i in range(0,len(pos_memoria)):
        posCache = pos_memoria[i] % tamanho_cache
        print("Linha",i,"| posição de memória desejada", pos_memoria[i])
        if(cache[posCache] == pos_memoria[i]):
            print("Status: Hit")
            hits += 1
        else:
            print("Status: Miss")
            misses += 1
            cache[posCache] = pos_memoria[i]
        print("Tamanho da Cache:",tamanho_cache)
        imprimir_cache(cache)
        print()
    
    taxa_acertos = (100 * hits) / len(pos_memoria)
    print("Memórias acessadas:", len(pos_memoria))
    print("Número de hits:", hits)                      
    print("Número de misses:", misses)
    print("Taxa de acertos (hits): ",format(taxa_acertos,".2f"),"%\n-------------------------------------------------------\n")





