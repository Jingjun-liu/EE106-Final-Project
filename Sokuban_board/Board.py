
man = '@'
box = '$'
des = '.'
emp = '-'
bar = '#'
up = [0, 1]
down = [0, -1]
right = [1, 0]
left = [-1, 0]

def getPiece(axis, board):
    p = mirror(axis)
    return Board[p[0]][p[1]]

def x(point):
    return point[0]

def y(point):
    return point[1]

def sumaxis(position, direction):
    return [x(position) + x(direction),
            y(position) + y(direction)]

def validdest(b, object, position, direction):
    """return the destination of a move.
       If it is barrier or is box when object is box
       return error. Position, direction, return value
       are all in [a, b] format"""
    dest = sumaxis(position, direction)
    dpiece = b[y(dest)][x(dest)]
    if dpiece == bar:
        print('Invalid move. Destination is barrier')
        return False
    elif dpiece == box:
        if object == box:
            print('Invalid move. Destination is box')
            return False
        elif object == man:
            return move_box(b, dest, direction)
    return True


    
def win():
    return "win"

def move_box(b, position, direction):
    if validdest(b, box, position, direction):
        pdes = sumaxis(position, direction)
        if b[x(pdes)][y(pdes)] == des:
            b.boxinDes += 1
        move(b, position, direction)
        if b.totaldes == b.boxinDes:
            win()
        return True
    print('Two boxes')
    return False

def move(b, position, direction):
    pdes = b.mirror(sumaxis(position, direction))
    pcur = b.mirror(position)
    b.board[y(pdes)] = b.board[y(pdes)][:x(pdes)] + b.board[y(pcur)][x(pcur)] + b.board[y(pdes)][x(pdes) + 1:]
    b.board[y(pcur)] = b.board[y(pcur)][:x(pcur)] + emp + b.board[y(pcur)][x(pcur) + 1:]



def move_man(b, position, direction):
    if not b[y(position)][x(position)] == man:
        print('Position do not have man')
        return b.manpoint
    if validdest(b, man, position, direction):
        move(b, position, direction)
        return sumaxis(position, direction)
    return b.manpoint

class Board:
    def __init__(self):
        map1 = open("map1.txt", "r")
        arrayBoard = map1.readlines()
        arrayBoard = [row.replace("\n",'').replace('"','') for row in arrayBoard]
        map1.close()
        self.board = arrayBoard
        self.rowNumber = len(arrayBoard)
        self.colNumber = len(arrayBoard[0])
        self.storemove = []
        self.storeundo = []
        self.pushtimes = 0
        self.boxinDes = 0
        self.totaldes = 0
        for row in arrayBoard:
            for piece in row:
                if piece == des:
                    self.totaldes += 1
        for rowi in range(self.rowNumber):
            for coli in range(self.colNumber):
                if self.board[rowi][coli] == man:
                    self.manpoint = [rowi + 1, coli + 1]


    def __str__(self):
        board = self.board
        output = ''
        for rowi in range(self.rowNumber):
            rowp = self.rowNumber - rowi - 1
            if rowp < 10:
                output += '{0}  '.format(rowp)
            elif rowp < 100:
                output += '{0} '.format(rowp)
            for coli in range(0, self.colNumber):
                output += '{0}  '.format(board[rowi][coli])
            output += '\n'
        colstr = '   '
        for coli in range(self.colNumber):
            if coli < 10:
                colstr += '{0}  '.format(coli)
            elif coli < 100:
                colstr += '{0} '.format(coli)
        output += colstr
        return output

    def __repr__(self):
        board = self.board
        output = ''
        for rowi in range(self.rowNumber):
            rowp = self.rowNumber - rowi - 1
            if rowi < 10:
                output += '{0}  '.format(rowi)
            elif rowi < 100:
                output += '{0} '.format(rowi)
            for coli in range(0, self.colNumber):
                output += '{0}  '.format(board[rowi][coli])
            output += '{0}'.format(rowp)
            output += '\n'
        colstr = '   '
        for coli in range(self.colNumber):
            if coli < 10:
                colstr += '{0}  '.format(coli)
            elif coli < 100:
                colstr += '{0} '.format(coli)
        output += colstr
        return output

    def __getitem__(self, item):
        return self.board[self.rowNumber - item - 1]

    def mirror(self, point):
        """AxistoArray"""
        return [x(point), self.rowNumber - y(point) - 1]




b = Board()
b
"""
bo = b.board
print(b)
move_man(b, [5, 6], up)
print(b)
"""
print(b)
while True:

    print('control your man by wsad:')
    s = raw_input()
    print(s)
    if s == 'w':
        b.manpoint = move_man(b, b.manpoint, up)
    elif s == 's':
        b.manpoint = move_man(b, b.manpoint, down)
    elif s == 'a':
        b.manpoint = move_man(b, b.manpoint, left)
    elif s == 'd':
        b.manpoint = move_man(b, b.manpoint, right)
    else:
        print("invalid input")
        continue
    print(b)




