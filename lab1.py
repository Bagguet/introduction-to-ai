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