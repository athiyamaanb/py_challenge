
def check_complete(matrix):
    #complete_flag = False
    for row in matrix:
        first_element = row[0]
        if first_element != ' ':
            row_check = True
            for column in row:
                if first_element != column:
                    row_check = False
                    break
            if row_check:
                return True
        #if len(set(row)) == 1 and set(row) != ' ':
        #    complete_flag = True
    #return complete_flag

def print_current_state(matrix):
    for row in matrix:
        print('|'.join(row))

def insert_element(matrix, row, column, value):
    if matrix_board[row][column] == ' ':
        matrix[row][column] = value
    else:
        print('An element is already present in the given position!')
        return
    print_current_state(matrix)

if __name__ == '__main__':

    matrix_board = [[' ',' ',' '],['0','0',' '], ['X','X','0']]
    print_current_state(matrix_board)

    player_sequence = ['p1','p1','p2']
    played = []

    print('Play Started.')

    for player in player_sequence:
        print('Player trying to play: ' + player)
        if len(played) >0 and played[-1] == player:
            print('Its not your turn!')
            pass
        else:
            print('Inserting element to the board...')
            insert_element(matrix_board, 1, 2,'0')
            played.append(player)

    print_current_state(matrix_board)
    if check_complete(matrix_board):
        print('Game Complete')
    else:
        print('Not Compelete')
