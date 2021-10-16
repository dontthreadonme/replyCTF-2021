import pprint as pp
""" This is what our heroes are facing. First two numbers are the height and the width of the grid in which the puzzle pieces will be placed, then all the pieces are listed in a random order.
Every piece is composed by 4 numbers each representing an edge of the piece: upper edge, under edge, left edge and right edge. Two pieces can be connected only if the edges are equal(i.e. in order to place a piece on the left of another piece then the right edge and the left edge respectively have to be equal).
Some pieces also have a character engraved on them. Solving the puzzle will reveal the key to the weapon.
h 200
w 200 """
f = open("puzzle.txt", "r")


""" up down left right """


targetup = []
target = []


def findup(piece):
    global targetup, pieces
    goal = piece[0]
    for each in pieces:
        if each[1] == goal:
            targetup = each
            findup(each)


def findleft(piece):
    global target, pieces
    goal = piece[2]
    for each in pieces:
        if each[3] == goal:
            target = each
            findleft(each)


def findnextright(piece):
    global pieces
    for each in range(len(pieces)):
        if piece[3] == pieces[each][2]:
            return pieces.pop(each)


def findnextdown(piece):
    global pieces
    for each in range(len(pieces)):
        if piece[1] == pieces[each][0]:
            return pieces.pop(each)


pieces = []
for line in f:
    piece = []
    for elem in line.split():
        piece.append(elem)
    pieces.append(piece)

findup(pieces[0])
findleft(targetup)

puzzle = []
for _ in range(200):
    puzzle.append([])

puzzle[0].append(target)

for i in range(199):
    for j in range(199):
        puzzle[i].append(findnextright(puzzle[i][j]))
    puzzle[i+1].append(findnextdown(puzzle[i][0]))


passw = []
for i in puzzle:
    for j in i:
        if len(j) > 4:
            passw += j[4]

out = open("answer.txt", "w")
print("".join(passw), file=out)
