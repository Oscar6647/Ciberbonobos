import chess

board = chess.Board()

mapa = board.piece_map()

print(mapa)

objetivo = input()

xy = objetivo.split(",")
poscicion = 8*(int(xy[1])-1)+(int(xy[0])-1)

print(poscicion)
print(xy)

mapa_objetivo = mapa.get((poscicion))

print(mapa_objetivo)