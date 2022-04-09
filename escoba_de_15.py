import random
import itertools

def subListas(lista):
    """
    arma una lista de todas las sublistas de la lista dada
    """
    resultado = []
    for k in range(1, len(lista) + 1):
        for listita in itertools.combinations(lista, k):
            resultado.append(list(listita))
    return resultado

def generarMazo():
    mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
    random.shuffle(mazo)
    return mazo

def repartir(mazo, jug1, jug2, jug3, jug4):
    for i in range(3):
        jug1.append(mazo.pop(0))
        jug2.append(mazo.pop(0))
        jug3.append(mazo.pop(0))
        jug4.append(mazo.pop(0))
    return mazo

def iniciarMesa(mazo, mesa):
    for i in range(4):
        mesa.append(mazo.pop(0))

def juegosPosibles(jug, mesa):
    combinaciones_mesa = subListas(mesa)
    juegos_que_suman_15 = []
    for carta_jugador in jug:
        for juego in combinaciones_mesa:
            suma_juego = carta_jugador
            for carta in juego:
                suma_juego = suma_juego + carta
            if suma_juego == 15:
                juegos_que_suman_15.append([carta_jugador] + juego)
    return juegos_que_suman_15

def elegirMejor(juegos):
    if juegos != []:
        mejor_juego = juegos[0]
        for juego in juegos[1:]:
            if len(juego) > len(mejor_juego):
                mejor_juego = juego
        return mejor_juego
    else:
        return []

def jugar(mesa, jug, basa):
    if jug != []:
        juegos = juegosPosibles(jug, mesa)
        mejor_juego = elegirMejor(juegos)
        if mejor_juego != []:
            basa.append(mejor_juego)
            jug.remove(mejor_juego[0])
            for carta in mejor_juego[1:]:
                mesa.remove(carta)
        else:
            mesa.append(jug.pop(0))

def jugarRonda(mesa, jug1, basa1, jug2, basa2, jug3, basa3, jug4, basa4):
    while jug1 != [] or jug2 != [] or jug3 != [] or jug4 != []:
        jugar(mesa, jug1, basa1)
        jugar(mesa, jug2, basa2)
        jugar(mesa, jug3, basa3)
        jugar(mesa, jug4, basa4)

def sumaPuntos(basa1, basa2, basa3, basa4):
    
    cartas_jug1 = 0
    for juego in basa1:
        cartas_jug1 = cartas_jug1 + len(juego)
        
    cartas_jug2 = 0
    for juego in basa2:
        cartas_jug2 = cartas_jug2 + len(juego)
        
    cartas_jug3 = 0
    for juego in basa3:
        cartas_jug3 = cartas_jug3 + len(juego)

    cartas_jug4 = 0
    for juego in basa4:
        cartas_jug4 = cartas_jug4 + len(juego)



    cartas_jugadores = [cartas_jug1, cartas_jug2, cartas_jug3, cartas_jug4]
    mayores_cartas = cartas_jugadores[0]
    for n_cartas in cartas_jugadores[1:]:
        if n_cartas > mayores_cartas:
            mayores_cartas = n_cartas
            
    mejores_jugadores = []
    for n_cartas in cartas_jugadores:
        if n_cartas == mayores_cartas:
            mejores_jugadores.append(cartas_jugadores.index(n_cartas))

    

    if len(mejores_jugadores) > 1:
        print("Empate")
        return [0, 0, 0, 0]
    else:
        puntos = [0] * 4
        puntos[mejores_jugadores[0]] = 1
        return puntos

if __name__ == "__main__":
    
    mesa = []
    
    jug1 = []
    jug2 = []
    jug3 = []
    jug4 = []
    
    basa1 = []
    basa2 = []
    basa3 = []
    basa4 = []
    
    mazo = generarMazo()
    mazo = repartir(mazo, jug1, jug2, jug3, jug4)
    iniciarMesa(mazo, mesa)
    
    jugarRonda(mesa, jug1, basa1, jug2, basa2, jug3, basa3, jug4, basa4)
    puntos = sumaPuntos(basa1, basa2, basa3, basa4)
    
    print("Basa 1", basa1)
    print("Basa 2", basa2)
    print("Basa 3", basa3)
    print("Basa 4", basa4)
    print("Puntos: (coordenada i = puntos del jugador i)")
    print(puntos)