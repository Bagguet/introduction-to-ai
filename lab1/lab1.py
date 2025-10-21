def wstep():
    lista = [1]

    slownik = {
        "1": lista.copy()
    }

    for i in range(2, 7):
        lista.append(i)
        slownik[str(i)] = lista.copy()
    print(slownik)

    maximium = 0
    maximu_key = ""
    for key, value in slownik.items():
        suma = sum(value)
        if suma > maximium:
            maximium = suma
            maximium_key = key
    print(f"klucz: {maximium_key}, suma: {maximium}")

from queue import Queue
def bfsZadanie1():
    nodes = {
        1: [2, 3],
        2: [1, 5],
        3: [1, 4],
        4: [3, 6],
        5: [2, 6, 8],
        6: [4, 5, 7, 8],
        7: [6],
        8: [5, 6]
    }
    visited = set()
    parent = {n: None for n in nodes}
    s = 1
    g = 8

    q = Queue()

    q.put(s)
    parent[s] = s
    while not q.empty():
        cur_n = q.get()
        if cur_n == g:
            break
        for nh in nodes[cur_n]:
            if nh not in visited:
                parent[nh] = cur_n
                visited.add(nh)
                q.put(nh)
    path = []
    cur_n = g
    while cur_n != s:
        path.append(cur_n)
        cur_n = parent[cur_n]
    path.reverse()
    print(f"najkrótsza trasa: {path}")
#bfsZadanie1()
